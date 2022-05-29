#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Program to retrieve practices
Uses a CSV file with the list of students, with this format:
"Usuario GitLab","Usuario Laboratorio",Usuario,"Nombre de usuario","Dirección de correo"
* Usuario GitLab is the name used for GitLab repos
* Usuario is the URJC user name

Example ofhow to run the script:
retrieve_repos.py --practice :all: --students ist-saro-2022.csv --cloning_dir ../../retrieved-2022
"""

import argparse
import csv
import json
import os
import subprocess
import urllib.request

from shutil import copyfile
from distutils.dir_util import copy_tree

from git.repo.base import Repo
from git.exc import GitCommandError

def add_api (practices):
    for number, practice in practices.items():
        practice['repo_api'] = practice['repo'].replace('/', '%2F')

practices = {
    "calculadora": {
        'repo': 'cursosweb/x-serv-13.6-calculadora',
        'repo_api': 'cursosweb%2Fx-serv-13.6-calculadora'
    },
    "redir": {
        'repo': 'cursosweb/x-serv-15.4-aplicacion-redirectora',
        'repo_api': 'cursosweb%2Fx-serv-15.4-aplicacion-redirectora',
    },
    "contentapp": {
        'repo': 'cursosweb/xserv-contentapp',
        'repo_api': 'cursosweb%2Fxserv-contentapp'
    },
    "django_cmsput": {
        'repo': 'cursosweb/x-serv-15.6-django-cms-put',
        'repo_api': 'cursosweb%2Fx-serv-15.6-django-cms-put'
    },
    "django_cmsusersput": {
        'repo': 'cursosweb/x-serv-15.8-cmsusersput',
        'repo_api': 'cursosweb%2Fx-serv-15.8-cmsusersput'
    },
    "django_cmspost": {
        'repo': 'cursosweb/practicas/server/django-cms-post',
        'repo_api': 'cursosweb%2Fpracticas%2Fserver%2Fdjango-cms-post'
    },
    "youtube": {
        'repo': 'cursosweb/practicas/server/youtube-descarga',
        'repo_api': 'cursosweb%2Fpracticas%2Fserver%2Fyoutube-descarga'
    },
    "django_youtube": {
        'repo': 'cursosweb/practicas/server/django-youtube',
        'repo_api': 'cursosweb%2Fpracticas%2Fserver%2Fdjango-youtube'
    },
    "django_cmscss2": {
        'repo': 'cursosweb/practicas/server/django-cms-css-2',
        'repo_api': 'cursosweb%2Fpracticas%2Fserver%2Fdjango-cms-css-2'
    },
    "1": {
        'repo': 'cursosweb/mini-1-acortadora',
        'repo_api': 'cursosweb%2Fmini-1-acortadora'
    },
    "2": {
        'repo': 'cursosweb/x-serv-18.2-practica2',
        'repo_api': 'cursosweb%2Fx-serv-18.2-practica2'
    }
}

add_api(practices)

def get_token() -> str:
    try:
        with open('token', 'r') as token_file:
            token: str = token_file.readline().rstrip()
            return token
    except FileNotFoundError:
        return ''

def get_forks(repo: str, token: str = ''):
    req_headers = {}
    if token != '':
        req_headers['PRIVATE-TOKEN'] = token
    # Pages are ints starting in 1, so these are just initialization values
    this_page, total_pages = 1, None
    forks = []
    while (total_pages is None) or (this_page <= total_pages):
        url = f"https://gitlab.etsit.urjc.es/api/v4/projects/{repo}/forks?per_page=50&page={this_page}"
        req = urllib.request.Request(url=url, headers=req_headers)
        with urllib.request.urlopen(req) as response:
            contents = response.read()
            resp_headers = response.info()
            total_pages = int(resp_headers['x-total-pages'])
            this_page += 1
            contents_str = contents.decode('utf8')
            forks = forks + json.loads(contents_str)
    return forks

def clone(url, dir, token=''):
#    auth_url = url.replace('https://', f"https://Api Read Access:{token}@", 1)
    auth_url = url.replace('https://', f"https://jesus.gonzalez.barahona:{token}@", 1)
    print("Cloning:", dir, auth_url)
    try:
        Repo.clone_from(auth_url, dir)
    except GitCommandError as err:
        print(f"Error: git error {err}")

def read_csv(file):
    students = {}
    with open(file, 'r', newline='') as cvsfile:
        rows = csv.DictReader(cvsfile)
        for row in rows:
            students[row['Usuario GitLab']] = {
                'user': row['Nombre de usuario'],
                'name': row['Usuario']
            }
            # print(f"{row['Usuario GitLab']}: {row['Nombre de usuario']}, {row['Usuario']}")
    return students

def run_tests(dir: str, solved_dir: str, silent: bool=False):
    """Run tests for this directory"""
    print("Running tests for", dir)
    # Copy tests to evaltests in analyzed directory
    tests_dir = os.path.join(solved_dir, 'tests')
    copy_tree(tests_dir, os.path.join(dir, 'evaltests'))
    # Copy check.py to analyzed directory
    copyfile(os.path.join(solved_dir, 'check.py'), os.path.join(dir, 'check.py'))
    test_call = ['python3', 'check.py', '--silent', '--testsdir', 'evaltests']
    if silent:
        test_call.append('--silent')
        stderr = subprocess.PIPE
    else:
        stderr = None
    result = subprocess.run(test_call,
                            cwd=dir, stdout=subprocess.PIPE,
                            stderr=stderr, text=True)
#    print("Tests result:", result.stdout.splitlines()[-1])
    print("Tests result:", result.stdout)
    if result.returncode == 0:
        print(f"Running tests OK: {dir}")
        return True
    else:
        print(f"Running tests Error: {dir}")
        return False

def parse_args():
    parser = argparse.ArgumentParser(description='Evaluate practices.')
    parser.add_argument('--silent', action='store_true',
                        help="silent output, only summary is written")
    parser.add_argument('--no_clone', action='store_true',
                        help="don't clone repos, assume repos were already cloned")
    parser.add_argument('--students', required=True,
                        help="name of csv file with students, exported from Moodle")
    parser.add_argument('--practice', default=2,
                        help="practice number (:all: to retrieve all practices")
    parser.add_argument('--cloning_dir', default='retrieved',
                        help="directory for cloning retrieved practices")
    parser.add_argument('--testing_dir', default='/tmp/p',
                        help="directory for tests")
    args = parser.parse_args()
    return(args)

def retrieve_practice(practice_id, cloning_dir, token):
    practice = practices[practice_id]
    forks = get_forks(repo=practice['repo_api'], token=token)
    repos_found = 0
    #    print(forks)

    students = read_csv(args.students)

    for fork in forks:
        # Each fork is a repo to consider
        fork_data = {
            'url': fork['http_url_to_repo'],
            'name': fork['namespace']['name'],
            'path': fork['namespace']['path']
        }
        if fork_data['path'] in students:
            # We're only interested in repos in the list of students
            print(f"Found: {fork_data['path']}")
            repos_found += 1
            if not args.no_clone:
                dir = os.path.join(cloning_dir, practice_id, fork_data['path'])
                clone(fork_data['url'], dir, token)
        # # Run tests in the cloned repo
        # print("About to run tests:", os.path.join(testing_dir, fork_data['path']))
        # run_tests(dir=os.path.join(testing_dir, fork_data['path']),
        #           solved_dir=practice['solved_dir'],
        #           silent=args.silent)
    print(f"Total forks: {len(forks)}, repos found: {repos_found}")


if __name__ == "__main__":
    args = parse_args()
    testing_dir = args.testing_dir
    cloning_dir = args.cloning_dir
    token: str = get_token()

    if args.practice == ':all:':
        practice_ids = practices.keys()
    else:
        practice_ids = [args.practice]
    for practice_id in practice_ids:
        print(f"Retrieving practice {practice_id}")
        retrieve_practice(practice_id, cloning_dir, token)

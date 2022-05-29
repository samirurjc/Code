#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Check repos retrieved (usually with retrieve_repos)
to help in evaluating practice work"""

import argparse
import csv
import os

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

def parse_args():
    parser = argparse.ArgumentParser(description='Evaluate practices.')
    parser.add_argument('--students', required=True,
                        help="name of csv file with students, exported from Moodle")
    parser.add_argument('--practice', default=2,
                        help="practice number (:all: to check all practices")
    parser.add_argument('--cloning_dir', default='retrieved',
                        help="directory where retrieved practices were cloned")
    args = parser.parse_args()
    return(args)

def practice_student(cloning_dir, practice, student):
    "Features of the practice, as pushed by student"

    if os.path.isdir(os.path.join(cloning_dir, practice, student)):
#        print(f"{student} delivered {practice}")
        return practice
    else:
        return None

def report_students(cloning_dir, practices_list, student):
    "Report fo rthe practices of a student"

    report = []
    for practice in practices_list:
        result = practice_student(cloning_dir, practice, student)
        if result is not None:
            report.append(result)
    return report

def read_students(file):
    students = {}
    with open(file, 'r', newline='') as cvsfile:
        rows = csv.DictReader(cvsfile)
        for row in rows:
            students[row['Usuario GitLab']] = {
                'user': row['Nombre de usuario'],
                'name': row['Usuario']
            }
    return students

def main():
    args = parse_args()
    students = read_students(args.students)
    cloning_dir = args.cloning_dir
    if args.practice == ':all:':
        practices_list = [practice for practice in practices]
    else:
        practices_list = [args.practice]
    for student in students:
        report = report_students(cloning_dir, practices_list, student)
        print(f"{student}: {len(report)}, {report}")

if __name__ == "__main__":
    main()
# Scripts for checking practices

## retrieve_repos.py

Retrieve repositories from the ETSIT GitLab instance which are forked from a template repository, and are in a list of students.

For each practice, there is a dictionary in `retrieve_repos.py`, `practices`, specifying the name of the template repository, and the name of the repository in the GitLab API.

For each subject, there is a CSV file with the list of students, which is retrieved from the corresponding activity in Moodle, with the format:

```
"Usuario GitLab","Usuario Laboratorio",Usuario,"Nombre de usuario","Dirección de correo"
```

* Usuario GitLab is the name used for GitLab repos
* Usuario is the URJC user name

Cloned repositories, by default, go to directory results/id (being `id` the identified of  the practice in the `practices` repository).

To run the script, a file `token` with a valid ETSIT GitLub token should be in the directory from which the script is run.

Note: The name of the repository in the GitLab API could be generated from the name of the repository, we should fix this in the future.
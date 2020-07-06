# Movie Rater API
API repository to deal with backend python API's

Repo created to expose REST API.

### Stack

- Django3
- Database (SQLite3)
- Django REST Framework

## Setup Virtual Environment

In "MovieRaterAPI" directory, run command "pip install virtualenv" and then "virtualenv venv" to create virtual environment "venv"

Setup and Activate Environment "venv" by command 

Mac/Linux

- python -m  venv __env__
- source __env__/bin/activate 

Windows
- python -m  venv __env__
- __env__\Scripts\activate

Whereas, env is environment name.

## How to install dependencies

```bash
$ pip install -r requirements.txt
```

## Deployment (Local + Heroku + AWS + GCP + Azure)

It is possible to deploy to local or to your own server.

## Run Application
```bash
$ python manage.py runserver
```

Additional command needs to run whenever you make changes in models file.
```bash
$ python manage.py migrate
$ python manage.py makemigrations
$ python manage.py migrate
```

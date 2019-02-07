# Checka

This is Django app that manages your home budget.

## Requirements
1. git client - [Install git client](https://www.atlassian.com/git/tutorials/install-git)
1. python 3.6 [Install python](https://www.python.org/downloads/)
2. pip 18.1 or higher - [Install pip](https://pip.pypa.io/en/stable/installing/)

## Instalation

### Clone
```
git clone git@github.com:alexshemesh/checka.git
cd checka
```
### Create virtual environment
```
python -m venv ~/.venvs/checka
```
### Activate virtual environment
```
source  ~/.venvs/checka/bin/activate
```
### Install requirements
```
pip install -r requirements.txt
```
### Generate DB
```
python manage.py migrate
```
### Run server
```
python manage.py runserver
```
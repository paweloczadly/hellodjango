#!/bin/bash
python3 manage.py migrate
python3 manage.py makemigrations hello
python3 manage.py sqlmigrate hello 0001
python3 manage.py runserver 0.0.0.0:8000

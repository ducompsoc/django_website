#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate
python3 create_admin.py
python3 manage.py collectstatic --noinput
gunicorn website.wsgi -b 0.0.0.0:8000

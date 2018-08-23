import json
import os
import subprocess
import sys

import django
from django.conf import settings as project_settings


def setup_django():

    # Not necessarily required as working directory is /django. May prevent future bugs however
    sys.path.append('/django')

    django.setup()


def create_new_migrations():

    # On every run, try to apply all migrations. May do nothing, but that's ok
    django.core.management.execute_from_command_line(['manage.py', 'makemigrations'])


def apply_migrations():
    django.core.management.execute_from_command_line(['manage.py', 'migrate'])


def create_admin_user():
    # Try to create admin user. Again in line with Python's philosophy, if this user already exists in the DB, it's fine
    with open(project_settings.SECRETS_FILE) as secrets_file:
        settings = json.load(secrets_file)

    try:
        admin_user = django.contrib.auth.models.User.objects.create_superuser(
           username=settings["ADMIN_USERNAME"],
           email=settings["ADMIN_EMAIL"],
           password=settings["ADMIN_PASSWORD"])

        admin_user.save()
    except django.db.utils.IntegrityError:
        print("Admin user already created")


def collect_static_files():
    django.core.management.execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])


def install_dev_requirements():
    print('Installing development requirements...')
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', os.path.join(project_settings.BASE_DIR,
                   os.environ['DEV_REQUIREMENTS_TXT'])])


def run_interface_server():
    subprocess.run(['gunicorn', 'website.wsgi', '-b', '0.0.0.0:8000'])


def start_django():
    setup_django()
    create_new_migrations()
    apply_migrations()
    create_admin_user()
    collect_static_files()

    if 'DEV_REQUIREMENTS_TXT' in os.environ:
        install_dev_requirements()

    run_interface_server()


if __name__ == '__main__':
    start_django()

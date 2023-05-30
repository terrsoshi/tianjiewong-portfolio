#!/bin/bash

echo "Making Migrations..."
/opt/venv/bin/python manage.py makemigrations --noinput

echo "Migrating database..."
/opt/venv/bin/python manage.py migrate --noinput

echo "Collecting Static Files..."
/opt/venv/bin/python manage.py collectstatic --noinput --clear

echo "Trying to create superuser..."
/opt/venv/bin/python manage.py createsuperuser --noinput

echo "Starting Django server..."
APP_PORT=${PORT:-8000}
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm backend.wsgi:application --bind "0.0.0.0:${APP_PORT}"

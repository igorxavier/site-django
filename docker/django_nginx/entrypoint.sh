#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input
#python manage.py tailwind build --no-input

python manage.py crontab add

service cron restart

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput

gunicorn base.wsgi:application -b :8081 --timeout 120 --workers=3 --threads=3 --worker-connections=1000 --worker-class=gevent
#!/bin/bash
python manage.py migrate

python manage.py collectstatic --clear --noinput

cp -r /app/collected_static/. /backend_static/static/

python manage.py load_from_csv_ingredients

python manage.py load_from_csv_tags

gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000

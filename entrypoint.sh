#!/usr/bin/env sh

echo "Prepare migrations"
python manage.py migrate --noinput
echo "Done migration"

echo "Prepare collectstatic"
python manage.py collectstatic --noinput
echo "Done collectstatic"

echo "Run the server"
gunicorn -b 0.0.0.0:8000 movies.wsgi:application --timeout 60 --log-level info -w 8 --max-requests 10000 

echo "Done"
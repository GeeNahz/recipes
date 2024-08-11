#!/bin/sh

>&2 echo "=== === ==="

# Wait for Postgres to be ready
./waitforpostgres.sh postgresdb

>&2 echo "=== === ==="

# Perform database migration
>&2 echo "=== Making database migrations ==="
python manage.py makemigrations
python manage.py migrate
>&2 echo "=== Operation successful ==="

>&2 echo "=== === ==="

# Create superuser
python manage.py createsu

>&2 echo "=== === ==="

# Collect static files
# python manage.py collectstatic --noinput

# >&2 echo "=== === ==="

# Start Django application with Gunicorn
>&2 echo "=== Starting server ==="
python manage.py runserver 0.0.0.0:8000
# gunicorn backend.wsgi:application --bind 0.0.0.0:8000

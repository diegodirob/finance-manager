#!/bin/bash
set -e

cd /code/finance-manager

echo "Running with mode $MODE"
export DJANGO_SETTINGS_MODULE="main.settings.$MODE"

if [ ${MODE} = "development" ]; then 
  python manage.py migrate
  python manage.py runserver 0.0.0.0:8000
fi

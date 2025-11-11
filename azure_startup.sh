#!/usr/bin/env bash
set -euo pipefail

# Use Python from Oryx environment if present
PY=${PYTHON:-python}

# Install dependencies (App Service Linux containers have pip)
$PY -m pip install --upgrade pip
$PY -m pip install -r requirements.txt

# Collect static files and run migrations
$PY manage.py collectstatic --noinput
$PY manage.py migrate --noinput

# Run gunicorn
PORT=${PORT:-8000}
exec gunicorn BlogBreeze.wsgi:application --bind 0.0.0.0:${PORT} --workers ${WEB_CONCURRENCY:-3}

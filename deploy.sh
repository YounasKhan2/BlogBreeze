#!/bin/bash

# Exit on error
set -e

echo "Running post-deployment script..."

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

echo "Post-deployment script completed successfully!"

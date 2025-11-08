# Deployment Guide

This guide covers deploying the BlogBreeze Django application to various platforms.

## Table of Contents
- [Pre-Deployment Checklist](#pre-deployment-checklist)
- [Deploying to Appwrite](#deploying-to-appwrite)
- [Deploying to Heroku](#deploying-to-heroku)
- [Deploying to PythonAnywhere](#deploying-to-pythonanywhere)
- [Post-Deployment Steps](#post-deployment-steps)

## Pre-Deployment Checklist

Before deploying, ensure you have:

- [ ] Updated `DEBUG = False` in production settings
- [ ] Set a strong `SECRET_KEY` (use environment variable)
- [ ] Configured `ALLOWED_HOSTS` with your domain
- [ ] Set up a production database (PostgreSQL recommended)
- [ ] Collected static files (`python manage.py collectstatic`)
- [ ] Run all migrations
- [ ] Tested the application locally
- [ ] Committed all changes to Git

## Deploying to Appwrite

### Step 1: Prepare Your Application

1. **Update settings for production**

Create a production settings file or use environment variables:

```python
# BlogBreeze/settings.py

import os
from pathlib import Path

DEBUG = os.environ.get('DEBUG', 'False') == 'True'
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'blogbreeze_db'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Static files
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# Media files
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
```

2. **Install WhiteNoise for static files**

```bash
pip install whitenoise
pip freeze > requirements.txt
```

Add to middleware in settings.py:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
    # ... rest of middleware
]
```

3. **Create a start script**

Create `start.sh`:
```bash
#!/bin/bash

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn
gunicorn BlogBreeze.wsgi:application --bind 0.0.0.0:$PORT
```

Make it executable:
```bash
chmod +x start.sh
```

### Step 2: Set Up Appwrite Project

1. **Create an Appwrite account** at https://appwrite.io

2. **Create a new project** in the Appwrite console

3. **Set up a PostgreSQL database**
   - Use Appwrite's database service or an external PostgreSQL provider
   - Note the connection details (host, port, database name, user, password)

### Step 3: Configure Environment Variables

In your Appwrite project settings, add these environment variables:

```
SECRET_KEY=your-generated-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.appwrite.io,your-custom-domain.com
DB_NAME=blogbreeze_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432
PORT=8000
```

### Step 4: Deploy Your Application

1. **Connect your Git repository** to Appwrite

2. **Configure build settings**:
   - Build command: `pip install -r requirements.txt`
   - Start command: `./start.sh` or `gunicorn BlogBreeze.wsgi:application --bind 0.0.0.0:$PORT`

3. **Deploy** and monitor the build logs

### Step 5: Post-Deployment

1. **Run migrations** (if not automated):
```bash
python manage.py migrate
```

2. **Create a superuser**:
```bash
python manage.py createsuperuser
```

3. **Create initial content**:
   - Login to admin panel
   - Create categories and tags
   - Create your first blog post

## Deploying to Heroku

### Step 1: Install Heroku CLI

Download and install from https://devcenter.heroku.com/articles/heroku-cli

### Step 2: Prepare Your Application

1. **Create Procfile**:
```
web: gunicorn BlogBreeze.wsgi --log-file -
release: python manage.py migrate
```

2. **Create runtime.txt**:
```
python-3.11.0
```

3. **Update requirements.txt**:
```bash
pip install gunicorn dj-database-url psycopg2-binary whitenoise
pip freeze > requirements.txt
```

4. **Update settings.py for Heroku**:
```python
import dj_database_url

# Database
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}
```

### Step 3: Deploy to Heroku

```bash
# Login to Heroku
heroku login

# Create a new Heroku app
heroku create your-app-name

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:mini

# Set environment variables
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS='your-app-name.herokuapp.com'

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser

# Open your app
heroku open
```

## Deploying to PythonAnywhere

### Step 1: Upload Your Code

1. Create a PythonAnywhere account at https://www.pythonanywhere.com
2. Open a Bash console
3. Clone your repository:
```bash
git clone https://github.com/yourusername/BlogBreeze.git
cd BlogBreeze
```

### Step 2: Set Up Virtual Environment

```bash
mkvirtualenv --python=/usr/bin/python3.10 blogbreeze-env
pip install -r requirements.txt
```

### Step 3: Configure Database

1. Go to the Databases tab
2. Create a PostgreSQL database (or use MySQL)
3. Note the connection details

### Step 4: Configure WSGI File

1. Go to the Web tab
2. Create a new web app
3. Choose "Manual configuration" with Python 3.10
4. Edit the WSGI configuration file:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/BlogBreeze'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'BlogBreeze.settings'
os.environ['SECRET_KEY'] = 'your-secret-key'
os.environ['DEBUG'] = 'False'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Step 5: Configure Static Files

In the Web tab, set up static file mappings:
- URL: `/static/`
- Directory: `/home/yourusername/BlogBreeze/staticfiles/`

- URL: `/media/`
- Directory: `/home/yourusername/BlogBreeze/media/`

### Step 6: Run Migrations

In a Bash console:
```bash
cd BlogBreeze
workon blogbreeze-env
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

### Step 7: Reload Web App

Click the "Reload" button in the Web tab.

## Post-Deployment Steps

### 1. Verify Deployment

- [ ] Visit your site and ensure it loads
- [ ] Test user registration and login
- [ ] Create a test blog post
- [ ] Test image upload
- [ ] Test commenting functionality
- [ ] Test search and filtering
- [ ] Check admin panel access

### 2. Set Up Monitoring

- Configure error logging
- Set up uptime monitoring
- Enable application performance monitoring

### 3. Configure Domain (Optional)

- Purchase a custom domain
- Configure DNS settings
- Update `ALLOWED_HOSTS` in settings
- Set up SSL certificate (usually automatic)

### 4. Create Initial Content

1. Login to admin panel
2. Create categories (e.g., Technology, Lifestyle, Travel)
3. Create tags (e.g., Python, Django, Web Development)
4. Create your first blog post
5. Test all functionality

### 5. Set Up Backups

- Configure automatic database backups
- Back up media files regularly
- Keep a local copy of your database

## Troubleshooting

### Static Files Not Loading

```bash
python manage.py collectstatic --noinput
```

Ensure WhiteNoise is installed and configured.

### Database Connection Errors

- Verify database credentials
- Check if database service is running
- Ensure database is accessible from your deployment platform

### 500 Internal Server Error

- Check application logs
- Verify `DEBUG=False` and `ALLOWED_HOSTS` are set correctly
- Ensure all migrations are run
- Check for missing environment variables

### Media Files Not Uploading

- Verify `MEDIA_ROOT` and `MEDIA_URL` are configured
- Check file permissions on media directory
- Ensure storage service has write permissions

## Security Best Practices

1. **Never commit sensitive data**
   - Use environment variables for secrets
   - Keep `.env` file in `.gitignore`

2. **Use strong passwords**
   - Generate strong `SECRET_KEY`
   - Use complex database passwords

3. **Enable HTTPS**
   - Use SSL certificates (Let's Encrypt is free)
   - Set `SECURE_SSL_REDIRECT = True`

4. **Keep dependencies updated**
   ```bash
   pip list --outdated
   pip install --upgrade package-name
   ```

5. **Regular backups**
   - Automate database backups
   - Back up media files
   - Test restore procedures

## Maintenance

### Updating the Application

```bash
# Pull latest changes
git pull origin main

# Install new dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Restart application
# (method depends on hosting platform)
```

### Database Maintenance

```bash
# Create backup
python manage.py dumpdata > backup.json

# Restore from backup
python manage.py loaddata backup.json
```

## Support

For deployment issues:
1. Check the platform's documentation
2. Review application logs
3. Search for error messages
4. Open an issue on GitHub

---

**Good luck with your deployment! 🚀**

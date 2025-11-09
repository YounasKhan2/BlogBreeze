# Render Deployment Checklist

Use this checklist to ensure smooth deployment to Render.com

## Pre-Deployment

- [ ] All code is committed to Git
- [ ] Code is pushed to GitHub
- [ ] `requirements.txt` is up to date
- [ ] `build.sh` file exists and is executable
- [ ] Settings are configured for production

## Render Setup

- [ ] Created Render.com account
- [ ] Connected GitHub account to Render
- [ ] Created PostgreSQL database
- [ ] Copied Internal Database URL

## Web Service Configuration

- [ ] Created new Web Service
- [ ] Connected correct GitHub repository
- [ ] Set Build Command: `./build.sh`
- [ ] Set Start Command: `gunicorn BlogBreeze.wsgi:application`
- [ ] Selected Free tier

## Environment Variables

- [ ] `PYTHON_VERSION` = `3.11.0`
- [ ] `SECRET_KEY` = (generated)
- [ ] `DEBUG` = `False`
- [ ] `DATABASE_URL` = (your database URL)

## Post-Deployment

- [ ] Deployment completed successfully
- [ ] App URL is accessible
- [ ] Created superuser via Shell
- [ ] Logged into admin panel
- [ ] Created at least one category
- [ ] Created at least one tag
- [ ] Created first blog post
- [ ] Tested all features:
  - [ ] Homepage loads
  - [ ] Blog post detail page works
  - [ ] Categories page works
  - [ ] Search works
  - [ ] User registration works
  - [ ] User login works
  - [ ] Image upload works

## Optional

- [ ] Set up custom domain
- [ ] Configure uptime monitoring
- [ ] Set up database backups
- [ ] Add Google Analytics (if needed)

## Troubleshooting Done

- [ ] Checked deployment logs
- [ ] Verified all environment variables
- [ ] Tested static files loading
- [ ] Tested media files upload
- [ ] Checked database connection

---

**Status**: ⬜ Not Started | 🟡 In Progress | ✅ Complete

**Deployment Date**: _______________

**App URL**: _______________

**Notes**:
_______________________________________________
_______________________________________________
_______________________________________________

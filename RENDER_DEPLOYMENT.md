# Deploy BlogBreeze to Render.com

This guide will walk you through deploying your Django blog to Render.com for FREE.

## Prerequisites

- A GitHub account
- Your code pushed to a GitHub repository
- A Render.com account (sign up at https://render.com)

## Step-by-Step Deployment Guide

### Step 1: Push Your Code to GitHub

If you haven't already, push your code to GitHub:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Prepare for Render deployment"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

### Step 2: Sign Up for Render

1. Go to https://render.com
2. Click "Get Started for Free"
3. Sign up with your GitHub account (recommended)
4. Authorize Render to access your repositories

### Step 3: Create a PostgreSQL Database

1. From your Render dashboard, click **"New +"**
2. Select **"PostgreSQL"**
3. Fill in the details:
   - **Name**: `blogbreeze-db` (or any name you prefer)
   - **Database**: `blogbreeze`
   - **User**: `blogbreeze` (auto-generated)
   - **Region**: Choose closest to your location
   - **PostgreSQL Version**: 16 (latest)
   - **Plan**: **Free** (select the free tier)
4. Click **"Create Database"**
5. Wait for the database to be created (takes ~1 minute)
6. **IMPORTANT**: Copy the **Internal Database URL** (you'll need this later)
   - It looks like: `postgresql://user:password@hostname/database`

### Step 4: Create a Web Service

1. From your Render dashboard, click **"New +"**
2. Select **"Web Service"**
3. Connect your GitHub repository:
   - If first time: Click "Connect account" and authorize Render
   - Find your repository in the list
   - Click **"Connect"**

4. Configure your web service:

   **Basic Settings:**
   - **Name**: `blogbreeze` (or your preferred name)
   - **Region**: Same as your database
   - **Branch**: `main` (or your default branch)
   - **Root Directory**: Leave blank
   - **Runtime**: **Python 3**
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn BlogBreeze.wsgi:application`

   **Instance Type:**
   - Select **Free** (this gives you 750 hours/month)

5. Click **"Advanced"** to add environment variables

### Step 5: Configure Environment Variables

Click **"Add Environment Variable"** and add these one by one:

| Key | Value | Notes |
|-----|-------|-------|
| `PYTHON_VERSION` | `3.11.0` | Python version |
| `SECRET_KEY` | Click "Generate" | Django secret key |
| `DEBUG` | `False` | Production mode |
| `DATABASE_URL` | Paste your Internal Database URL | From Step 3 |
| `ALLOWED_HOSTS` | Leave empty for now | Will be auto-configured |

**Important**: 
- For `SECRET_KEY`, click the "Generate" button to create a secure random key
- For `DATABASE_URL`, paste the **Internal Database URL** you copied from Step 3

### Step 6: Deploy!

1. Click **"Create Web Service"**
2. Render will now:
   - Clone your repository
   - Install dependencies
   - Run migrations
   - Collect static files
   - Start your application

3. Watch the deployment logs (this takes 2-5 minutes)
4. Once you see "Your service is live 🎉", your app is deployed!

### Step 7: Get Your App URL

1. At the top of your service page, you'll see your app URL
2. It will look like: `https://blogbreeze-xxxx.onrender.com`
3. Click on it to open your blog!

### Step 8: Create a Superuser

You need to create an admin account to manage your blog:

1. In your Render dashboard, go to your web service
2. Click on **"Shell"** in the left sidebar
3. Wait for the shell to connect
4. Run this command:
   ```bash
   python manage.py createsuperuser
   ```
5. Follow the prompts to create your admin account:
   - Username: (your choice)
   - Email: (your email)
   - Password: (strong password)
   - Password confirmation: (same password)

### Step 9: Access Admin Panel

1. Go to your app URL + `/admin`
   - Example: `https://blogbreeze-xxxx.onrender.com/admin`
2. Login with the superuser credentials you just created
3. Start creating content:
   - Add categories
   - Add tags
   - Create your first blog post!

## Important Notes

### Free Tier Limitations

- **Spin Down**: Your app will spin down after 15 minutes of inactivity
- **Wake Up Time**: Takes ~30 seconds to wake up when someone visits
- **Database**: 1GB storage limit on free tier
- **Bandwidth**: 100GB/month

### Keeping Your App Awake (Optional)

If you want to prevent spin-down, you can:

1. **Upgrade to paid plan** ($7/month) - recommended for production
2. **Use a ping service** (free but not recommended):
   - UptimeRobot.com
   - Cron-job.org
   - Set them to ping your URL every 14 minutes

### Custom Domain (Optional)

To use your own domain:

1. Go to your web service settings
2. Click "Custom Domain"
3. Add your domain
4. Update your DNS records as instructed
5. Render will automatically provision SSL certificate

## Troubleshooting

### Build Failed

**Check the logs** for specific errors:
- Missing dependencies? Update `requirements.txt`
- Python version issues? Check `PYTHON_VERSION` env var
- Database connection? Verify `DATABASE_URL`

### 500 Internal Server Error

1. Check the logs in Render dashboard
2. Verify all environment variables are set correctly
3. Make sure `DEBUG=False` and `ALLOWED_HOSTS` is configured

### Static Files Not Loading

1. Run in Shell:
   ```bash
   python manage.py collectstatic --no-input
   ```
2. Check that WhiteNoise is in `MIDDLEWARE` in settings.py

### Database Connection Error

1. Verify `DATABASE_URL` is correct
2. Make sure you copied the **Internal Database URL** (not External)
3. Check that database and web service are in the same region

### App is Slow

- Free tier spins down after 15 minutes
- First request after spin-down takes ~30 seconds
- Consider upgrading to paid tier for always-on service

## Updating Your App

When you make changes to your code:

```bash
# Make your changes
git add .
git commit -m "Your update message"
git push origin main
```

Render will automatically:
- Detect the push
- Rebuild your app
- Deploy the new version
- Takes 2-5 minutes

## Monitoring

In your Render dashboard you can:
- View real-time logs
- Monitor resource usage
- Check deployment history
- View metrics and analytics

## Next Steps

1. **Create Content**: Add categories, tags, and blog posts
2. **Customize**: Update site name, colors, and branding
3. **Test**: Try all features (posting, commenting, search)
4. **Share**: Share your blog URL with others!
5. **Monitor**: Keep an eye on logs and performance

## Cost Optimization

**Free Tier is Perfect For:**
- Personal blogs
- Portfolio projects
- Learning and testing
- Low-traffic sites

**Consider Upgrading When:**
- You get consistent traffic (no spin-down)
- You need faster response times
- You want custom domain with SSL
- You need more than 1GB database storage

## Support

- **Render Docs**: https://render.com/docs
- **Render Community**: https://community.render.com
- **Django Docs**: https://docs.djangoproject.com

## Security Checklist

- [x] `DEBUG=False` in production
- [x] Strong `SECRET_KEY` generated
- [x] Database credentials secured
- [x] HTTPS enabled (automatic on Render)
- [x] Static files served via WhiteNoise
- [ ] Regular backups (set up database backups in Render)
- [ ] Monitor logs for suspicious activity

---

## Quick Reference

**Your URLs:**
- App: `https://your-service-name.onrender.com`
- Admin: `https://your-service-name.onrender.com/admin`
- Database: Check Render dashboard

**Useful Commands (in Render Shell):**
```bash
# Create superuser
python manage.py createsuperuser

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input

# Check Django version
python manage.py --version

# Open Django shell
python manage.py shell
```

---

**Congratulations! Your blog is now live! 🎉**

Visit your URL and start blogging!

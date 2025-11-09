# 🚀 Render Deployment - Quick Start (5 Minutes)

Follow these steps to deploy your blog to Render.com in under 5 minutes!

## Step 1: Push to GitHub (1 min)

```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

## Step 2: Create Database (1 min)

1. Go to https://render.com → Sign up/Login
2. Click **"New +"** → **"PostgreSQL"**
3. Name: `blogbreeze-db`
4. Plan: **Free**
5. Click **"Create Database"**
6. **Copy the "Internal Database URL"** (you'll need this!)

## Step 3: Create Web Service (2 min)

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repo
3. Settings:
   - Name: `blogbreeze`
   - Build Command: `./build.sh`
   - Start Command: `gunicorn BlogBreeze.wsgi:application`
   - Plan: **Free**

4. Add Environment Variables:
   - `PYTHON_VERSION` = `3.11.0`
   - `SECRET_KEY` = Click "Generate"
   - `DEBUG` = `False`
   - `DATABASE_URL` = Paste your database URL from Step 2

5. Click **"Create Web Service"**

## Step 4: Wait for Deployment (2-3 min)

Watch the logs. When you see "Your service is live 🎉", you're done!

## Step 5: Create Admin Account (1 min)

1. In your service page, click **"Shell"**
2. Run:
   ```bash
   python manage.py createsuperuser
   ```
3. Enter username, email, and password

## Step 6: Start Blogging! 🎉

1. Visit: `https://your-app-name.onrender.com/admin`
2. Login with your superuser account
3. Create categories and your first post!

---

## Your App URLs

- **Blog**: `https://your-app-name.onrender.com`
- **Admin**: `https://your-app-name.onrender.com/admin`

## Need Help?

See the full guide: [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)

---

**That's it! Your blog is live! 🚀**

# Quick Start Guide

Get BlogBreeze up and running in 5 minutes!

## Prerequisites

- Python 3.8+ installed
- Git installed
- Basic command line knowledge

## Installation Steps

### 1. Clone and Navigate

```bash
git clone <your-repo-url>
cd BlogBreeze
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Database

```bash
python manage.py migrate
```

### 5. Create Admin User

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 6. Run Development Server

```bash
python manage.py runserver
```

### 7. Access the Application

Open your browser and visit:
- **Main Site**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/

## First Steps

### 1. Create Categories

1. Login to admin panel (http://localhost:8000/admin/)
2. Click on "Categories"
3. Add categories like:
   - Technology
   - Lifestyle
   - Travel
   - Food
   - etc.

### 2. Create Tags

1. In admin panel, click on "Tags"
2. Add tags like:
   - Python
   - Django
   - Web Development
   - Tutorial
   - etc.

### 3. Create Your First Post

**Option A: Through Admin Panel**
1. Go to admin panel
2. Click "Posts" → "Add Post"
3. Fill in the details and save

**Option B: Through Frontend**
1. Register a new account or login
2. Your account will be a "Reader" by default
3. Go to admin panel and change your role to "Author"
4. Click "Create Post" in the navigation menu
5. Fill in the post details:
   - Title
   - Content (use the rich text editor)
   - Category
   - Tags
   - Featured Image (optional)
   - Status (Draft or Published)
6. Click "Create Post"

### 4. Test Features

- **View Posts**: Visit the home page
- **Search**: Use the search bar
- **Filter**: Click on categories or tags
- **Comment**: Login and comment on a post
- **Dashboard**: Access your author dashboard

## Common Commands

```bash
# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Open Django shell
python manage.py shell
```

## Default User Roles

- **Admin**: Full access to everything
- **Author**: Can create and manage their own posts
- **Reader**: Can view posts and comment

To change a user's role:
1. Go to admin panel
2. Click "User profiles"
3. Find the user and change their role

## Troubleshooting

**Issue**: `ModuleNotFoundError`
- **Solution**: Make sure virtual environment is activated and dependencies are installed

**Issue**: Database errors
- **Solution**: Run `python manage.py migrate`

**Issue**: Static files not loading
- **Solution**: Run `python manage.py collectstatic`

**Issue**: Can't create posts
- **Solution**: Make sure your user has "Author" or "Admin" role

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment instructions
- Customize the design in templates and static files
- Add more features as needed

## Need Help?

- Check the documentation
- Review Django documentation: https://docs.djangoproject.com/
- Open an issue on GitHub

---

**Happy Blogging! 📝**

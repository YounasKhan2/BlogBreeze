# BlogBreeze - Django Blog Platform

A full-featured blog platform built with Django that provides user authentication, role-based permissions, rich text editing, and comprehensive content management capabilities.

## Features

### User Management
- **User Registration & Authentication**: Secure user registration with email validation and login/logout functionality
- **Role-Based Access Control**: Three user roles (Admin, Author, Reader) with distinct permissions
- **User Profiles**: Extended user profiles with bio, avatar, and role information
- **Author Dashboard**: Dedicated dashboard for authors to manage their posts

### Content Management
- **Rich Text Editor**: CKEditor integration for creating beautifully formatted blog posts
- **Post Management**: Create, edit, delete, and publish blog posts
- **Draft & Published States**: Save posts as drafts before publishing
- **Featured Images**: Upload and display featured images for posts (JPEG, PNG, GIF up to 5MB)
- **Categories & Tags**: Organize posts with categories and tags for easy navigation
- **SEO-Friendly URLs**: Automatic slug generation from titles for better SEO

### Interaction Features
- **Commenting System**: Authenticated users can comment on published posts
- **Comment Moderation**: Admins can approve or disapprove comments
- **Search Functionality**: Full-text search across post titles and content
- **Filtering**: Filter posts by category or tag
- **Pagination**: Paginated post lists (10 posts per page)

### Admin Features
- **Customized Admin Panel**: Enhanced Django admin with bulk actions and filters
- **Post Management**: Bulk status changes, filtering by category/status/author
- **Comment Moderation**: Bulk approve/disapprove comments
- **User Management**: Manage users and assign roles

### Technical Features
- **Responsive Design**: Bootstrap 5 for mobile-friendly interface
- **Signal Handlers**: Post publication notifications
- **Media File Handling**: Secure image upload and storage
- **Database Support**: SQLite (development) and PostgreSQL (production)

## Technology Stack

- **Backend**: Django 5.2.8
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Rich Text Editor**: CKEditor
- **Image Processing**: Pillow
- **Deployment**: Appwrite (or Heroku/PythonAnywhere)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Local Setup

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd BlogBreeze
```

2. **Create and activate virtual environment**

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables** (optional)

Create a `.env` file in the project root:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create a superuser**
```bash
python manage.py createsuperuser
```

7. **Create initial categories and tags** (optional)

Access the Django admin panel at `http://localhost:8000/admin/` and create some categories and tags.

8. **Run the development server**
```bash
python manage.py runserver
```

9. **Access the application**

Open your browser and navigate to:
- Main site: `http://localhost:8000/`
- Admin panel: `http://localhost:8000/admin/`

## Project Structure

```
BlogBreeze/
├── BlogBreeze/              # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
├── blog/                    # Blog application
│   ├── models.py           # Post, Category, Tag, Comment models
│   ├── views.py            # View logic
│   ├── forms.py            # PostForm, CommentForm
│   ├── urls.py             # Blog URL patterns
│   ├── admin.py            # Admin customization
│   ├── signals.py          # Post publication signals
│   └── migrations/         # Database migrations
├── accounts/                # User management application
│   ├── models.py           # UserProfile model
│   ├── views.py            # Auth views, dashboard
│   ├── forms.py            # Registration, login forms
│   ├── urls.py             # Account URL patterns
│   ├── admin.py            # User admin customization
│   └── mixins.py           # Permission mixins
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── blog/               # Blog templates
│   └── accounts/           # Account templates
├── static/                  # Static files (CSS, JS, images)
├── media/                   # User-uploaded content
│   └── posts/              # Post featured images
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Usage

### User Roles

1. **Admin**
   - Full access to all posts, comments, categories, and tags
   - Can manage all users and content
   - Access to Django admin panel

2. **Author**
   - Can create, edit, and delete their own posts
   - Can publish or save posts as drafts
   - Access to author dashboard
   - Can view all published posts and comment

3. **Reader**
   - Can view all published posts
   - Can comment on posts
   - Cannot create or edit posts

### Creating a Blog Post

1. Register or login as an Author or Admin
2. Navigate to "Create Post" from the navigation menu
3. Fill in the post details:
   - Title (required)
   - Content (required, rich text editor)
   - Category (required)
   - Tags (optional)
   - Featured Image (optional, max 5MB)
   - Status (Draft or Published)
4. Click "Create Post"

### Managing Posts

- **Author Dashboard**: Access from the navigation menu to see all your posts
- **Edit Post**: Click "Edit Post" button on post detail page
- **Delete Post**: Click "Delete Post" button on post detail page
- **Publish Draft**: Edit the post and change status to "Published"

### Commenting

1. Login to your account
2. Navigate to any published post
3. Scroll to the comments section
4. Write your comment and click "Post Comment"

### Searching Posts

Use the search bar in the navigation menu to search for posts by title or content.

### Filtering Posts

- Click on a category name to see all posts in that category
- Click on a tag to see all posts with that tag

## Deployment

### 🚀 Deploy to Render.com (FREE - Recommended)

**Ready to deploy?** 

👉 **[START_HERE.md](START_HERE.md)** - Choose your deployment path

**Quick Links:**
- ⚡ [5-Minute Quick Deploy](RENDER_QUICKSTART.md)
- 📚 [Detailed Deployment Guide](RENDER_DEPLOYMENT.md)
- ✅ [Deployment Checklist](DEPLOYMENT_CHECKLIST.md)

**Why Render?**
- ✅ Free tier (no credit card required)
- ✅ Automatic HTTPS & SSL
- ✅ PostgreSQL database included
- ✅ Auto-deploy from GitHub
- ✅ Easy setup (5 minutes)

### Deploying to Appwrite

1. **Prepare for deployment**

Update `BlogBreeze/settings.py` for production:
```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')
```

2. **Configure database**

For PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
```

3. **Configure static files**

Install WhiteNoise:
```bash
pip install whitenoise
```

Add to `MIDDLEWARE` in settings.py:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... other middleware
]
```

Configure static files:
```python
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

4. **Collect static files**
```bash
python manage.py collectstatic --noinput
```

5. **Set environment variables**

Configure these environment variables in your Appwrite deployment:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `False`
- `ALLOWED_HOSTS`: Your domain names
- `DB_NAME`: Database name
- `DB_USER`: Database user
- `DB_PASSWORD`: Database password
- `DB_HOST`: Database host
- `DB_PORT`: Database port

6. **Run migrations on production**
```bash
python manage.py migrate
```

7. **Create superuser on production**
```bash
python manage.py createsuperuser
```

### Alternative Deployment Options

#### Heroku

1. Install Heroku CLI and login
2. Create `Procfile`:
```
web: gunicorn BlogBreeze.wsgi --log-file -
release: python manage.py migrate
```

3. Create `runtime.txt`:
```
python-3.11.0
```

4. Deploy:
```bash
heroku create your-app-name
git push heroku main
heroku run python manage.py createsuperuser
```

#### PythonAnywhere

1. Upload your code to PythonAnywhere
2. Create a virtual environment
3. Install dependencies
4. Configure WSGI file
5. Set up static files mapping
6. Reload your web app

## Configuration

### Environment Variables

Create a `.env` file for local development:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (PostgreSQL)
DB_NAME=blogbreeze_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

# Email (optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### CKEditor Configuration

CKEditor is configured in `settings.py`. You can customize the toolbar and features:

```python
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source'],
        ],
        'height': 400,
        'width': '100%',
    },
}
```

## Testing

Run the Django test suite:

```bash
python manage.py test
```

Run tests for specific apps:

```bash
python manage.py test blog
python manage.py test accounts
```

## Security Considerations

- Change `SECRET_KEY` in production
- Set `DEBUG = False` in production
- Use HTTPS in production
- Configure `ALLOWED_HOSTS` properly
- Use strong passwords for admin accounts
- Keep dependencies updated
- Enable CSRF protection (enabled by default)
- Validate all user inputs (implemented in forms)

## Troubleshooting

### Common Issues

**Issue**: Images not displaying
- **Solution**: Ensure `MEDIA_URL` and `MEDIA_ROOT` are configured in settings.py
- Check that media URL patterns are added in urls.py for development

**Issue**: Static files not loading
- **Solution**: Run `python manage.py collectstatic`
- Ensure `STATIC_URL` and `STATIC_ROOT` are configured

**Issue**: Database errors
- **Solution**: Run `python manage.py migrate`
- Check database connection settings

**Issue**: Permission denied errors
- **Solution**: Ensure user has the correct role assigned
- Check permission mixins in views

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django framework and community
- Bootstrap for responsive design
- CKEditor for rich text editing
- All contributors and users

## Contact

For questions or support, please open an issue on GitHub or contact the maintainers.

## Screenshots

### Home Page
The home page displays a paginated list of published blog posts with featured images, categories, and tags.

### Post Detail
Individual post pages show the full content, comments section, and edit/delete options for authors.

### Author Dashboard
Authors can manage all their posts, view statistics, and quickly create new content.

### Admin Panel
Customized Django admin interface for managing posts, comments, categories, tags, and users.

---

**Built with ❤️ using Django**

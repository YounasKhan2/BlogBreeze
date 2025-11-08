"""
Deployment Preparation Script
Run this script before deploying to production
"""
import os
import sys
from pathlib import Path

def print_header(text):
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)

def print_section(text):
    print(f"\n{text}")
    print("-" * 70)

def check_files():
    """Check if all necessary files exist"""
    print_section("Checking Required Files...")
    
    required_files = [
        'README.md',
        'DEPLOYMENT.md',
        'QUICKSTART.md',
        'LICENSE',
        'requirements.txt',
        'Procfile',
        'runtime.txt',
        '.gitignore',
        'manage.py',
        'BlogBreeze/settings.py',
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} - MISSING!")
            all_exist = False
    
    return all_exist

def check_migrations():
    """Check if migrations are up to date"""
    print_section("Checking Migrations...")
    
    os.system('python manage.py makemigrations --dry-run --check')
    print("  ℹ If you see 'No changes detected', migrations are up to date")

def generate_secret_key():
    """Generate a new SECRET_KEY"""
    print_section("Generating New SECRET_KEY...")
    
    try:
        from django.core.management.utils import get_random_secret_key
        secret_key = get_random_secret_key()
        print(f"\n  Your new SECRET_KEY:")
        print(f"  {secret_key}")
        print("\n  ⚠️  IMPORTANT: Save this key securely!")
        print("  Add it to your environment variables as SECRET_KEY")
        return secret_key
    except Exception as e:
        print(f"  ✗ Error generating key: {e}")
        return None

def check_settings():
    """Check settings for production readiness"""
    print_section("Checking Settings...")
    
    warnings = []
    
    # Check if settings.py exists
    settings_file = 'BlogBreeze/settings.py'
    if os.path.exists(settings_file):
        with open(settings_file, 'r') as f:
            content = f.read()
            
            # Check DEBUG
            if "DEBUG = True" in content:
                warnings.append("DEBUG is set to True (should be False in production)")
            
            # Check SECRET_KEY
            if "django-insecure" in content:
                warnings.append("SECRET_KEY contains 'django-insecure' (generate new key)")
            
            # Check ALLOWED_HOSTS
            if "ALLOWED_HOSTS = []" in content:
                warnings.append("ALLOWED_HOSTS is empty (add your domain)")
    
    if warnings:
        print("  ⚠️  Warnings found:")
        for warning in warnings:
            print(f"     - {warning}")
    else:
        print("  ✓ Settings look good for development")
    
    print("\n  ℹ Remember to update these for production:")
    print("     - Set DEBUG = False")
    print("     - Use environment variable for SECRET_KEY")
    print("     - Add your domain to ALLOWED_HOSTS")

def check_dependencies():
    """Check if all dependencies are installed"""
    print_section("Checking Dependencies...")
    
    try:
        import django
        print(f"  ✓ Django {django.get_version()}")
    except ImportError:
        print("  ✗ Django not installed")
    
    try:
        import PIL
        print(f"  ✓ Pillow installed")
    except ImportError:
        print("  ✗ Pillow not installed")
    
    try:
        import ckeditor
        print(f"  ✓ django-ckeditor installed")
    except ImportError:
        print("  ✗ django-ckeditor not installed")

def show_git_commands():
    """Show Git commands for pushing to repository"""
    print_section("Git Commands")
    
    print("""
  To push your project to GitHub:
  
  1. Create a new repository on GitHub
  
  2. Run these commands:
     
     git init
     git add .
     git commit -m "Initial commit: Complete Django blog platform"
     git branch -M main
     git remote add origin https://github.com/yourusername/BlogBreeze.git
     git push -u origin main
  
  3. Replace 'yourusername/BlogBreeze' with your actual repository URL
    """)

def show_deployment_steps():
    """Show deployment steps"""
    print_section("Deployment Steps")
    
    print("""
  For Appwrite Deployment:
  
  1. Create an Appwrite account at https://appwrite.io
  2. Create a new project
  3. Set up PostgreSQL database
  4. Configure environment variables:
     - SECRET_KEY (use the generated key above)
     - DEBUG=False
     - ALLOWED_HOSTS=your-domain.com
     - Database credentials (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
  5. Connect your Git repository
  6. Deploy!
  
  For detailed instructions, see DEPLOYMENT.md
    """)

def main():
    print_header("BlogBreeze - Deployment Preparation")
    
    print("""
  This script will help you prepare your Django blog platform for deployment.
  It will check your project files, generate a new SECRET_KEY, and provide
  deployment instructions.
    """)
    
    # Run checks
    files_ok = check_files()
    
    if not files_ok:
        print("\n  ⚠️  Some required files are missing!")
        print("  Please ensure all files are present before deploying.")
        return
    
    check_dependencies()
    check_migrations()
    check_settings()
    
    # Generate new SECRET_KEY
    secret_key = generate_secret_key()
    
    # Show next steps
    show_git_commands()
    show_deployment_steps()
    
    print_header("Summary")
    print("""
  ✓ All required files are present
  ✓ New SECRET_KEY generated
  ✓ Ready for deployment!
  
  Next Steps:
  1. Update settings.py for production (or use environment variables)
  2. Push your code to GitHub
  3. Deploy to Appwrite (or your chosen platform)
  4. Run migrations on production
  5. Create superuser
  6. Test your deployment
  
  For detailed instructions, see:
  - DEPLOYMENT.md for deployment guide
  - PRE_DEPLOYMENT_CHECKLIST.md for checklist
  - QUICKSTART.md for quick start guide
  
  Good luck with your deployment! 🚀
    """)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nScript interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nError: {e}")
        sys.exit(1)

# 🔑 Render Environment Variables Guide

## Required Environment Variables

You need to add **4 environment variables** in your Render web service. Here's exactly what to do:

---

## 1. PYTHON_VERSION

### What it is:
Tells Render which Python version to use

### Value to enter:
```
3.11.0
```

### How to get it:
Just type it! No generation needed.

### Steps:
1. In Render, click "Add Environment Variable"
2. Key: `PYTHON_VERSION`
3. Value: `3.11.0`
4. Click "Save"

---

## 2. SECRET_KEY

### What it is:
Django's secret key for security (encryption, sessions, etc.)

### How to get it:
**Render will generate it for you!**

### Steps:
1. In Render, click "Add Environment Variable"
2. Key: `SECRET_KEY`
3. Click the **"Generate"** button (Render creates a random secure key)
4. Click "Save"

### ⚠️ Important:
- **DO NOT** use your local SECRET_KEY from settings.py
- **DO NOT** share this key with anyone
- Let Render generate a new one

---

## 3. DEBUG

### What it is:
Controls Django debug mode (must be False in production)

### Value to enter:
```
False
```

### How to get it:
Just type it!

### Steps:
1. In Render, click "Add Environment Variable"
2. Key: `DEBUG`
3. Value: `False` (capital F)
4. Click "Save"

### ⚠️ Important:
- Must be exactly `False` (capital F)
- Never set to `True` in production

---

## 4. DATABASE_URL

### What it is:
Connection string to your PostgreSQL database

### How to get it:
**Copy from your Render PostgreSQL database**

### Steps:

#### First, create the database:
1. In Render dashboard, click **"New +"**
2. Select **"PostgreSQL"**
3. Name: `blogbreeze-db`
4. Plan: **Free**
5. Click **"Create Database"**
6. Wait ~1 minute for creation

#### Then, copy the URL:
1. Go to your database page
2. Scroll down to **"Connections"** section
3. Find **"Internal Database URL"**
4. Click the **copy icon** 📋
5. It looks like:
   ```
   postgresql://user:password@hostname/database
   ```

#### Add to web service:
1. Go to your web service settings
2. Click "Add Environment Variable"
3. Key: `DATABASE_URL`
4. Value: **Paste** the Internal Database URL
5. Click "Save"

### ⚠️ Important:
- Use **Internal Database URL** (not External)
- Copy the entire URL
- Don't modify it

---

## Visual Guide: Where to Find Each Value

### SECRET_KEY
```
Render Dashboard → Web Service → Environment
→ Add Environment Variable
→ Key: SECRET_KEY
→ Click "Generate" button ← Render creates it!
```

### DATABASE_URL
```
Render Dashboard → PostgreSQL Database
→ Scroll to "Connections"
→ Find "Internal Database URL"
→ Click copy icon 📋
→ Paste in web service environment variables
```

### PYTHON_VERSION & DEBUG
```
Just type them manually:
- PYTHON_VERSION = 3.11.0
- DEBUG = False
```

---

## Complete Environment Variables Table

| Key | Value | Where to Get It |
|-----|-------|-----------------|
| `PYTHON_VERSION` | `3.11.0` | Type it manually |
| `SECRET_KEY` | (auto-generated) | Click "Generate" in Render |
| `DEBUG` | `False` | Type it manually |
| `DATABASE_URL` | `postgresql://...` | Copy from database page |

---

## Step-by-Step: Adding Environment Variables

### When Creating Web Service:

1. **After connecting your GitHub repo**, scroll to "Environment Variables"

2. **Click "Add Environment Variable"** and add each one:

   **First Variable:**
   - Key: `PYTHON_VERSION`
   - Value: `3.11.0`
   - Click outside the field

   **Second Variable:**
   - Key: `SECRET_KEY`
   - Click **"Generate"** button (Render fills it automatically)
   - Click outside the field

   **Third Variable:**
   - Key: `DEBUG`
   - Value: `False`
   - Click outside the field

   **Fourth Variable:**
   - Key: `DATABASE_URL`
   - Value: Paste your database URL
   - Click outside the field

3. **Click "Create Web Service"** at the bottom

---

## After Adding Variables

Your environment variables section should look like this:

```
PYTHON_VERSION = 3.11.0
SECRET_KEY = ••••••••••••••••••••••••••••••••••••••••
DEBUG = False
DATABASE_URL = postgresql://blogbreeze:••••••@dpg-xxxxx/blogbreeze
```

(The dots represent hidden values for security)

---

## Common Mistakes to Avoid

### ❌ Wrong:
- Using your local SECRET_KEY
- Setting DEBUG to `True`
- Using External Database URL
- Forgetting to click "Generate" for SECRET_KEY
- Typing DATABASE_URL manually

### ✅ Correct:
- Let Render generate SECRET_KEY
- Set DEBUG to `False`
- Use Internal Database URL
- Copy-paste DATABASE_URL exactly
- All 4 variables are set

---

## How to Get DATABASE_URL (Detailed)

### Step 1: Create Database
```
Render Dashboard
  ↓
Click "New +"
  ↓
Select "PostgreSQL"
  ↓
Fill in:
  - Name: blogbreeze-db
  - Database: blogbreeze
  - User: (auto-filled)
  - Region: (choose closest)
  - Plan: Free
  ↓
Click "Create Database"
  ↓
Wait ~1 minute
```

### Step 2: Copy Internal URL
```
Database Page
  ↓
Scroll to "Connections" section
  ↓
Find "Internal Database URL"
  ↓
Click copy icon 📋
  ↓
URL copied to clipboard!
```

### Step 3: Add to Web Service
```
Web Service Settings
  ↓
Environment Variables
  ↓
Add Environment Variable
  ↓
Key: DATABASE_URL
Value: Paste (Ctrl+V)
  ↓
Save
```

---

## Verification Checklist

After adding all variables, verify:

- [ ] `PYTHON_VERSION` = `3.11.0`
- [ ] `SECRET_KEY` = (long random string, generated by Render)
- [ ] `DEBUG` = `False` (capital F)
- [ ] `DATABASE_URL` = `postgresql://...` (starts with postgresql://)
- [ ] All 4 variables are present
- [ ] No typos in variable names

---

## What If I Make a Mistake?

### To Edit a Variable:
1. Go to web service settings
2. Find "Environment Variables"
3. Click the variable you want to edit
4. Update the value
5. Click "Save Changes"
6. Render will redeploy automatically

### To Delete a Variable:
1. Click the trash icon next to the variable
2. Confirm deletion
3. Add the correct one

---

## Security Notes

### Keep These Secret:
- ✅ SECRET_KEY
- ✅ DATABASE_URL

### Safe to Share:
- ✅ PYTHON_VERSION
- ✅ DEBUG (when set to False)

### Never:
- ❌ Commit environment variables to Git
- ❌ Share SECRET_KEY publicly
- ❌ Share DATABASE_URL publicly
- ❌ Screenshot environment variables with values visible

---

## Testing Your Variables

After deployment, check if variables are working:

### In Render Shell:
```bash
# Access the shell from your service page
python manage.py shell

# Then run:
from django.conf import settings
print(settings.DEBUG)  # Should print: False
print(settings.DATABASES['default']['NAME'])  # Should print: blogbreeze
```

If these work, your variables are set correctly!

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────┐
│  RENDER ENVIRONMENT VARIABLES                   │
├─────────────────────────────────────────────────┤
│                                                 │
│  1. PYTHON_VERSION = 3.11.0                     │
│     → Type manually                             │
│                                                 │
│  2. SECRET_KEY = (generated)                    │
│     → Click "Generate" button                   │
│                                                 │
│  3. DEBUG = False                               │
│     → Type manually                             │
│                                                 │
│  4. DATABASE_URL = postgresql://...             │
│     → Copy from database page                   │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## Need Help?

### Can't find Internal Database URL?
1. Go to your PostgreSQL database in Render
2. Look for "Connections" section
3. It's labeled "Internal Database URL"
4. Click the copy icon

### Generate button not working?
1. Make sure you're in the web service (not database)
2. The button appears next to the Value field
3. Try refreshing the page

### Variables not saving?
1. Make sure to click outside the field after entering
2. Scroll down and click "Create Web Service"
3. Don't navigate away before saving

---

## Summary

You need **4 environment variables**:

1. **PYTHON_VERSION** - Type: `3.11.0`
2. **SECRET_KEY** - Click: "Generate"
3. **DEBUG** - Type: `False`
4. **DATABASE_URL** - Copy from database

**That's it!** These 4 variables are all you need to deploy.

---

**Ready to add them? Follow the steps above! 🚀**

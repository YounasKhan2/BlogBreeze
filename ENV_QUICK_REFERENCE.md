# 🎯 Environment Variables - Quick Reference

## The 4 Variables You Need

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│  Variable 1: PYTHON_VERSION                                │
│  ─────────────────────────────                             │
│  Value: 3.11.0                                             │
│  How: Just type it                                         │
│                                                            │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Variable 2: SECRET_KEY                                    │
│  ─────────────────────────                                 │
│  Value: (Render generates it)                              │
│  How: Click "Generate" button                              │
│                                                            │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Variable 3: DEBUG                                         │
│  ─────────────────────────                                 │
│  Value: False                                              │
│  How: Just type it                                         │
│                                                            │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Variable 4: DATABASE_URL                                  │
│  ─────────────────────────                                 │
│  Value: postgresql://user:pass@host/db                     │
│  How: Copy from database page                              │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## Copy-Paste Values

### PYTHON_VERSION
```
3.11.0
```

### DEBUG
```
False
```

### SECRET_KEY
```
Click "Generate" - don't type anything!
```

### DATABASE_URL
```
Copy from: Database → Connections → Internal Database URL
```

---

## Where to Add Them

```
Render Dashboard
    ↓
Your Web Service
    ↓
Environment (tab)
    ↓
Add Environment Variable (button)
    ↓
Enter Key and Value
    ↓
Save
```

---

## Visual Guide

### 1. Type These Manually:
```
PYTHON_VERSION = 3.11.0
DEBUG = False
```

### 2. Generate This:
```
SECRET_KEY = [Click "Generate" button]
```

### 3. Copy This:
```
DATABASE_URL = [Copy from database page]
```

---

## Database URL Location

```
Render Dashboard
    ↓
PostgreSQL Database (blogbreeze-db)
    ↓
Scroll down to "Connections"
    ↓
Find "Internal Database URL"
    ↓
Click copy icon 📋
    ↓
Paste in web service
```

---

## Checklist

Before deploying, verify:

- [ ] PYTHON_VERSION = `3.11.0` ✓
- [ ] SECRET_KEY = (long random string) ✓
- [ ] DEBUG = `False` ✓
- [ ] DATABASE_URL = `postgresql://...` ✓

---

## Common Issues

### Issue: Can't find DATABASE_URL
**Solution**: Create PostgreSQL database first, then copy URL

### Issue: Generate button not working
**Solution**: Make sure you're in web service settings, not database

### Issue: Variables not saving
**Solution**: Click outside field, then click "Create Web Service"

---

## Need More Details?

See: [RENDER_ENV_VARIABLES.md](RENDER_ENV_VARIABLES.md)

---

**That's all you need! 4 simple variables! 🎉**

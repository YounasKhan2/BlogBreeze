# Image Storage Verification for Production

## ✅ Configuration Status

### Django Settings (BlogBreeze/settings.py)

**Media Files Configuration:**
```python
# Local Development (default)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Production (Azure Blob Storage)
if AZURE_ACCOUNT_NAME and AZURE_MEDIA_CONTAINER:
    DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
    MEDIA_URL = f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_CONTAINER}/"
```

**Required Environment Variables for Production:**
- ✅ `AZURE_ACCOUNT_NAME` - Your Azure Storage account name
- ✅ `AZURE_ACCOUNT_KEY` - Your Azure Storage account key
- ✅ `AZURE_MEDIA_CONTAINER` or `AZURE_CONTAINER` - Container name (e.g., 'media')
- ✅ `AZURE_STORAGE_CONNECTION_STRING` (optional alternative)

### Template Image References

All templates correctly use Django's `.url` property:
- ✅ `{{ post.featured_image.url }}` - Returns full URL to image
- ✅ Works with both local storage and Azure Blob Storage
- ✅ Fallback to placeholder images when no image is uploaded

**Templates Verified:**
1. ✅ `post_list.html` - Hero image and post cards
2. ✅ `post_detail.html` - Post header image and related posts
3. ✅ `category_posts.html` - Category post images
4. ✅ `tag_posts.html` - Tag post images
5. ✅ `search_results.html` - Search result images
6. ✅ `post_form.html` - Image upload and preview
7. ✅ `post_confirm_delete.html` - Image preview on delete

### How It Works

**Development (Local):**
- Images stored in: `media/` folder
- Accessed via: `http://localhost:8000/media/filename.jpg`
- Django serves media files directly

**Production (Azure):**
- Images uploaded to: Azure Blob Storage container
- Accessed via: `https://{account}.blob.core.windows.net/{container}/filename.jpg`
- Azure serves images with CDN capabilities
- No Django involvement in serving images (better performance)

## 🔍 Verification Checklist

### Before Deployment:
- [x] `django-storages` installed (in requirements.txt)
- [x] `azure-storage-blob` installed (in requirements.txt)
- [x] Settings configured to use Azure Blob Storage
- [x] Templates use `.url` property (not hardcoded paths)
- [x] Fallback images for posts without featured images

### After Deployment:
- [ ] Verify Azure Storage account exists
- [ ] Verify container exists (e.g., 'media')
- [ ] Verify container has public read access for blobs
- [ ] Set environment variables in Azure App Service:
  - `AZURE_ACCOUNT_NAME`
  - `AZURE_ACCOUNT_KEY`
  - `AZURE_MEDIA_CONTAINER`
- [ ] Test uploading an image through admin/post form
- [ ] Verify image displays on post detail page
- [ ] Verify image displays on post list page
- [ ] Check browser network tab for correct image URLs

## 🛠️ Azure Blob Storage Setup

### 1. Create Storage Account (if not exists)
```bash
az storage account create \
  --name <storage-account-name> \
  --resource-group <resource-group> \
  --location <location> \
  --sku Standard_LRS
```

### 2. Create Container
```bash
az storage container create \
  --name media \
  --account-name <storage-account-name> \
  --public-access blob
```

### 3. Get Account Key
```bash
az storage account keys list \
  --account-name <storage-account-name> \
  --resource-group <resource-group>
```

### 4. Set Environment Variables in Azure App Service
```bash
az webapp config appsettings set \
  --name <app-name> \
  --resource-group <resource-group> \
  --settings \
    AZURE_ACCOUNT_NAME="<storage-account-name>" \
    AZURE_ACCOUNT_KEY="<account-key>" \
    AZURE_MEDIA_CONTAINER="media"
```

## 🐛 Troubleshooting

### Images Not Displaying in Production

**Issue 1: 404 errors for images**
- Check: Container has public read access
- Fix: `az storage container set-permission --name media --public-access blob`

**Issue 2: Images upload but don't display**
- Check: Environment variables are set correctly
- Check: `MEDIA_URL` in settings matches Azure blob URL
- Fix: Verify `AZURE_ACCOUNT_NAME` and `AZURE_MEDIA_CONTAINER` are correct

**Issue 3: Permission denied errors**
- Check: `AZURE_ACCOUNT_KEY` is correct
- Check: Storage account allows access
- Fix: Regenerate and update account key

**Issue 4: Images work locally but not in production**
- Check: `DEFAULT_FILE_STORAGE` is set to Azure backend
- Check: Environment variables are present in production
- Fix: Ensure all Azure env vars are set in App Service configuration

### Testing Image URLs

**Expected URL format:**
```
https://<account-name>.blob.core.windows.net/media/<filename>
```

**Check in browser console:**
```javascript
// Should show Azure blob URL, not /media/
document.querySelector('img').src
```

## 📝 Current Status

**Dependencies Installed:** ✅
- django-storages==1.14.6
- azure-storage-blob==12.27.1

**Settings Configured:** ✅
- Conditional Azure Blob Storage setup
- Falls back to local storage in development

**Templates Updated:** ✅
- All use `.url` property
- Responsive image sizing
- Fallback placeholders

**Next Steps:**
1. Deploy to Azure App Service
2. Configure Azure Storage environment variables
3. Test image upload and display
4. Verify images load from Azure Blob Storage

---

**Status:** ✅ Ready for production deployment
**Last Updated:** 2024

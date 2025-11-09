# Cloudinary Setup for BlogBreeze

## Why Cloudinary?
Render's free tier has ephemeral filesystem - uploaded files are deleted on every redeploy. Cloudinary provides persistent cloud storage for images.

## Setup Steps:

### 1. Create Cloudinary Account
1. Go to https://cloudinary.com/users/register_free
2. Sign up for a free account
3. After login, go to Dashboard

### 2. Get Your Credentials
From the Cloudinary Dashboard, copy:
- **Cloud Name**
- **API Key**
- **API Secret**

### 3. Add Environment Variables in Render
Go to your Render service → Environment and add:

```
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 4. Deploy
The code changes are already committed. Just trigger a redeploy in Render.

## How It Works:
- In production (DEBUG=False): Images upload to Cloudinary
- In development (DEBUG=True): Images save locally to `/media/`
- CKEditor uploads go through Cloudinary storage
- All existing and new images will be stored permanently

## Testing:
1. After deployment, create a new blog post
2. Upload an image in the content editor
3. Publish the post
4. Image should display correctly and persist after redeployment

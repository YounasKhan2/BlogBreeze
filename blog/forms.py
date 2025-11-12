from django import forms
from django.utils.text import slugify
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Form for creating and editing blog posts"""
    
    class Meta:
        model = Post
        fields = ['title', 'description', 'content', 'category', 'tags', 'status', 'featured_image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-border-light dark:border-border-dark bg-background-light dark:bg-background-dark text-text-light dark:text-text-dark focus:outline-none focus:ring-2 focus:ring-primary',
                'placeholder': 'Enter post title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-border-light dark:border-border-dark bg-background-light dark:bg-background-dark text-text-light dark:text-text-dark focus:outline-none focus:ring-2 focus:ring-primary',
                'rows': 3,
                'maxlength': 300,
                'placeholder': 'Enter a short description (max 300 characters)'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-border-light dark:border-border-dark bg-background-light dark:bg-background-dark text-text-light dark:text-text-dark focus:outline-none focus:ring-2 focus:ring-primary',
                'rows': 10
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-border-light dark:border-border-dark bg-background-light dark:bg-background-dark text-text-light dark:text-text-dark focus:outline-none focus:ring-2 focus:ring-primary'
            }),
            'tags': forms.CheckboxSelectMultiple(),
            'status': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-border-light dark:border-border-dark bg-background-light dark:bg-background-dark text-text-light dark:text-text-dark focus:outline-none focus:ring-2 focus:ring-primary'
            }),
            'featured_image': forms.FileInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-border-light dark:border-border-dark bg-background-light dark:bg-background-dark text-text-light dark:text-text-dark focus:outline-none focus:ring-2 focus:ring-primary file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-primary file:text-white hover:file:bg-opacity-90',
                'accept': 'image/jpeg,image/png,image/gif'
            })
        }
        labels = {
            'title': 'Post Title',
            'description': 'Short Description',
            'content': 'Content',
            'category': 'Category',
            'tags': 'Tags',
            'status': 'Status',
            'featured_image': 'Featured Image'
        }
        help_texts = {
            'title': 'Enter a descriptive title for your post',
            'description': 'Brief summary of your post (optional, max 300 characters)',
            'content': 'Write your post content (supports rich text)',
            'category': 'Select a category for your post',
            'tags': 'Select relevant tags for your post',
            'status': 'Choose whether to save as draft or publish',
            'featured_image': 'Upload an image (JPEG, PNG, or GIF, max 5MB)'
        }
    
    def clean_title(self):
        """Validate that title is not empty and has reasonable length"""
        title = self.cleaned_data.get('title')
        if not title or not title.strip():
            raise forms.ValidationError('Title cannot be empty.')
        if len(title.strip()) < 3:
            raise forms.ValidationError('Title must be at least 3 characters long.')
        return title.strip()
    
    def clean_content(self):
        """Validate that content is not empty"""
        content = self.cleaned_data.get('content')
        if not content or not content.strip():
            raise forms.ValidationError('Content cannot be empty.')
        if len(content.strip()) < 10:
            raise forms.ValidationError('Content must be at least 10 characters long.')
        return content.strip()
    
    def clean_featured_image(self):
        """Validate image file type and size"""
        image = self.cleaned_data.get('featured_image')
        
        if image:
            # Check file size (max 5MB)
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError('Image file size cannot exceed 5MB.')
            
            # Check file type
            valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
            file_extension = image.name.split('.')[-1].lower()
            
            if file_extension not in valid_extensions:
                raise forms.ValidationError(
                    f'Invalid file type. Allowed types: {", ".join(valid_extensions).upper()}'
                )
            
            # Validate MIME type
            valid_mime_types = ['image/jpeg', 'image/png', 'image/gif']
            if hasattr(image, 'content_type') and image.content_type not in valid_mime_types:
                raise forms.ValidationError('Invalid image format.')
        
        return image
    
    def clean_category(self):
        """Validate that a category is selected"""
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('Please select a category for your post.')
        return category
    
    def save(self, commit=True):
        """Override save to auto-generate slug from title"""
        instance = super().save(commit=False)
        
        # Auto-generate slug from title if not already set or if title changed
        if not instance.slug or (instance.pk and instance.title):
            base_slug = slugify(instance.title)
            slug = base_slug
            counter = 1
            
            # Ensure slug uniqueness
            while Post.objects.filter(slug=slug).exclude(pk=instance.pk).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            
            instance.slug = slug
        
        if commit:
            instance.save()
            # Save many-to-many relationships
            self.save_m2m()
        
        return instance


class CommentForm(forms.ModelForm):
    """Form for creating comments on blog posts"""
    
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your comment here...'
            })
        }
        labels = {
            'content': 'Your Comment'
        }
    
    def clean_content(self):
        """Validate that comment content is not empty and has minimum length"""
        content = self.cleaned_data.get('content')
        
        if not content or not content.strip():
            raise forms.ValidationError('Comment cannot be empty.')
        
        if len(content.strip()) < 3:
            raise forms.ValidationError('Comment must be at least 3 characters long.')
        
        if len(content.strip()) > 1000:
            raise forms.ValidationError('Comment cannot exceed 1000 characters.')
        
        return content.strip()

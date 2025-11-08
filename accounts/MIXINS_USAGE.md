# Permission Mixins and Decorators Usage Guide

This document provides examples of how to use the permission mixins and decorators implemented in `accounts/mixins.py`.

## Available Components

### 1. RoleRequiredMixin
Restricts class-based views to users with specific roles.

**Example:**
```python
from django.views.generic import ListView
from accounts.mixins import RoleRequiredMixin
from blog.models import Post

class AuthorDashboardView(RoleRequiredMixin, ListView):
    model = Post
    template_name = 'accounts/dashboard.html'
    required_roles = ['author', 'admin']  # Only authors and admins can access
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
```

### 2. AuthorRequiredMixin
Restricts views to the post author or admin users.

**Example:**
```python
from django.views.generic import UpdateView
from accounts.mixins import AuthorRequiredMixin
from blog.models import Post

class PostUpdateView(AuthorRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'category', 'tags', 'status']
    template_name = 'blog/post_form.html'
    
    # The mixin automatically checks if request.user is the post author or admin
```

### 3. role_required decorator
Function-based view decorator for role restrictions.

**Example:**
```python
from django.shortcuts import render
from accounts.mixins import role_required

@role_required(['author', 'admin'])
def create_post(request):
    # Only authors and admins can access this view
    return render(request, 'blog/post_form.html')
```

### 4. author_required decorator
Function-based view decorator for author/admin restrictions.

**Example:**
```python
from django.shortcuts import get_object_or_404, render
from accounts.mixins import author_required
from blog.models import Post

@author_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    # Additional check for post ownership
    if post.author != request.user and request.user.profile.role != 'admin':
        raise PermissionDenied('You can only edit your own posts')
    
    return render(request, 'blog/post_form.html', {'post': post})
```

## Permission Logic

### RoleRequiredMixin
- Checks if user is authenticated
- Verifies user has a valid profile
- Ensures user's role is in the `required_roles` list
- Displays appropriate error messages
- Raises `PermissionDenied` if checks fail

### AuthorRequiredMixin
- Checks if user is authenticated
- Verifies user has a valid profile
- Allows access if user is the post author
- Allows access if user has 'admin' role
- Displays appropriate error messages
- Raises `PermissionDenied` if checks fail

## Error Handling

All mixins and decorators include:
- User-friendly error messages via Django messages framework
- Proper exception handling with `PermissionDenied`
- Automatic redirect to login page for unauthenticated users
- Clear feedback about required permissions

## Requirements Satisfied

This implementation satisfies the following requirements:
- **2.1**: Admin role has full access to all content
- **2.2**: Author role can create, edit, and delete their own posts
- **2.3**: Reader role has limited permissions
- **2.4**: Unauthorized actions are denied with appropriate error messages

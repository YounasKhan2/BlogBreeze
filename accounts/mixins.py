"""
Permission mixins and decorators for role-based access control.
"""
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.contrib import messages
from functools import wraps


class RoleRequiredMixin(LoginRequiredMixin):
    """
    Mixin to verify user has one of the required roles.
    
    Usage:
        class MyView(RoleRequiredMixin, View):
            required_roles = ['author', 'admin']
    
    Attributes:
        required_roles: List of role names that are allowed to access the view
    """
    required_roles = []
    
    def dispatch(self, request, *args, **kwargs):
        """
        Check if user has required role before dispatching the request.
        """
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        # Check if user has a profile
        if not hasattr(request.user, 'profile'):
            messages.error(request, 'Your account does not have a valid profile.')
            raise PermissionDenied('User profile not found')
        
        # Check if user has one of the required roles
        user_role = request.user.profile.role
        if user_role not in self.required_roles:
            messages.error(
                request,
                f'You do not have permission to access this page. '
                f'Required role: {", ".join(self.required_roles)}'
            )
            raise PermissionDenied(
                f'User role "{user_role}" is not in required roles: {self.required_roles}'
            )
        
        return super().dispatch(request, *args, **kwargs)


class AuthorRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Mixin to check if user is the author of the post or an admin.
    
    Usage:
        class PostUpdateView(AuthorRequiredMixin, UpdateView):
            model = Post
    
    This mixin expects the view to have access to a Post object.
    It works with DetailView, UpdateView, DeleteView, etc.
    """
    
    def test_func(self):
        """
        Test if user is the post author or has admin role.
        """
        # Get the post object
        post = self.get_object()
        user = self.request.user
        
        # Check if user has a profile
        if not hasattr(user, 'profile'):
            return False
        
        # Allow if user is the author
        if post.author == user:
            return True
        
        # Allow if user has admin role
        if user.profile.role == 'admin':
            return True
        
        return False
    
    def handle_no_permission(self):
        """
        Handle permission denied with appropriate error message.
        """
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                'You do not have permission to modify this post. '
                'Only the author or an admin can perform this action.'
            )
        return super().handle_no_permission()


def role_required(roles):
    """
    Decorator to restrict function-based views to specific roles.
    
    Usage:
        @role_required(['author', 'admin'])
        def my_view(request):
            ...
    
    Args:
        roles: List of role names that are allowed to access the view
    
    Returns:
        Decorated view function
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # Check if user is authenticated
            if not request.user.is_authenticated:
                messages.error(request, 'You must be logged in to access this page.')
                raise PermissionDenied('Authentication required')
            
            # Check if user has a profile
            if not hasattr(request.user, 'profile'):
                messages.error(request, 'Your account does not have a valid profile.')
                raise PermissionDenied('User profile not found')
            
            # Check if user has one of the required roles
            user_role = request.user.profile.role
            if user_role not in roles:
                messages.error(
                    request,
                    f'You do not have permission to access this page. '
                    f'Required role: {", ".join(roles)}'
                )
                raise PermissionDenied(
                    f'User role "{user_role}" is not in required roles: {roles}'
                )
            
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def author_required(view_func):
    """
    Decorator to restrict function-based views to post author or admin.
    
    Usage:
        @author_required
        def edit_post(request, slug):
            post = get_object_or_404(Post, slug=slug)
            ...
    
    Note: This decorator expects the view to retrieve the post object
    and check permissions manually, or use the class-based AuthorRequiredMixin instead.
    
    Args:
        view_func: The view function to decorate
    
    Returns:
        Decorated view function
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to access this page.')
            raise PermissionDenied('Authentication required')
        
        # Check if user has a profile
        if not hasattr(request.user, 'profile'):
            messages.error(request, 'Your account does not have a valid profile.')
            raise PermissionDenied('User profile not found')
        
        # Note: Actual post ownership check should be done in the view
        # This decorator only ensures authentication and profile existence
        # The view should use AuthorRequiredMixin for class-based views
        
        return view_func(request, *args, **kwargs)
    return wrapper

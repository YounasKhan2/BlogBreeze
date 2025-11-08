from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.db.models import Q
from .forms import UserRegistrationForm
from .mixins import RoleRequiredMixin
from blog.models import Post


class UserRegistrationView(CreateView):
    """
    View for user registration with automatic Reader role assignment.
    """
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        """
        Handle successful form submission.
        """
        response = super().form_valid(form)
        messages.success(
            self.request,
            'Registration successful! You can now log in with your credentials.'
        )
        return response
    
    def form_invalid(self, form):
        """
        Handle form validation errors.
        """
        messages.error(
            self.request,
            'Please correct the errors below.'
        )
        return super().form_invalid(form)


class UserLoginView(LoginView):
    """
    Custom login view using Django's built-in LoginView.
    """
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        """
        Handle successful login.
        """
        messages.success(self.request, f'Welcome back, {form.get_user().username}!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """
        Handle login errors.
        """
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)


def user_logout_view(request):
    """
    Logout view that terminates the user session and redirects to home page.
    """
    username = request.user.username if request.user.is_authenticated else None
    logout(request)
    
    if username:
        messages.success(request, f'Goodbye, {username}! You have been logged out.')
    
    return redirect('blog:post_list')


class AuthorDashboardView(RoleRequiredMixin, ListView):
    """
    Dashboard view for authors and admins to manage their posts.
    Displays all posts created by the current user with statistics.
    """
    model = Post
    template_name = 'accounts/dashboard.html'
    context_object_name = 'posts'
    required_roles = ['author', 'admin']
    paginate_by = 10
    
    def get_queryset(self):
        """
        Return all posts created by the current user.
        Optimize query with select_related for author and category.
        """
        return Post.objects.filter(
            author=self.request.user
        ).select_related(
            'author', 'category'
        ).prefetch_related(
            'tags'
        ).order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        """
        Add post statistics to the context.
        """
        context = super().get_context_data(**kwargs)
        
        # Get all user posts for statistics
        user_posts = Post.objects.filter(author=self.request.user)
        
        # Calculate draft and published counts
        context['draft_count'] = user_posts.filter(status='draft').count()
        context['published_count'] = user_posts.filter(status='published').count()
        context['total_count'] = user_posts.count()
        
        return context

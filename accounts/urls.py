from django.urls import path
from .views import UserRegistrationView, UserLoginView, user_logout_view, AuthorDashboardView

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout_view, name='logout'),
    path('dashboard/', AuthorDashboardView.as_view(), name='dashboard'),
]

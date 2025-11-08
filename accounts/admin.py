from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    """
    Inline admin for UserProfile to display within User admin.
    """
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fields = ('role', 'bio', 'avatar')


class UserAdmin(BaseUserAdmin):
    """
    Extended User admin with inline UserProfile.
    """
    inlines = (UserProfileInline,)


# Unregister the default User admin and register our custom one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Also register UserProfile separately for direct access
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'bio_preview')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email', 'bio')
    
    def bio_preview(self, obj):
        """Display first 50 characters of bio."""
        return obj.bio[:50] + '...' if len(obj.bio) > 50 else obj.bio
    bio_preview.short_description = 'Bio'

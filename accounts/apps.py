from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    
    def ready(self):
        """
        Import signals when the app is ready to ensure they are registered.
        """
        import accounts.models  # noqa

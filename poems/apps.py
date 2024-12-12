# poems/apps.py
from django.apps import AppConfig

class PoemsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'poems'

    def ready(self):
        import poems.signals  # Import the signals module

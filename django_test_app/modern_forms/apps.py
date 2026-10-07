from typing import final

from django.apps import AppConfig


@final
class ModernFormsConfig(AppConfig):
    """Config for modern_forms app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modern_forms'

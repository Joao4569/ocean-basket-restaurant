"""Import AppConfig from django apps"""
from django.apps import AppConfig


class OnlineBookingConfig(AppConfig):
    """Allocate auto field for django model and name app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'online_booking'

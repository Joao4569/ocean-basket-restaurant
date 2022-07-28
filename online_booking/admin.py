"""
Standard Django built-in imports plus custom import as follows:
Import CustomerBookingDetails model from models.py to register model
"""
from django.contrib import admin
from .models import CustomerDetails


admin.site.register(CustomerDetails)

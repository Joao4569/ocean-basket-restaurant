"""
Standard Django built-in imports plus custom import as follows:
Import CustomerBookingDetails model from models.py to register model
"""
from django.contrib import admin
from .models import CustomerBookingDetails


admin.site.register(CustomerBookingDetails)

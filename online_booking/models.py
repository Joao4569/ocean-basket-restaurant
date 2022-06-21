"""
Import models folder in order to create tables for our database
"""
from django.db import models


class CustomerBookingDetails(models.Model):
    """
    Create a database model for online customer booking details
    """
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    contact_number = models.IntegerField(null=False, blank=False)
    email = models.CharField(max_length=50)
    number_of_seats = models.SmallIntegerField(null=False, blank=False)
    service = models.CharField(max_length=6, null=False, blank=False)
    date = models.DateField(null=False, blank=False)

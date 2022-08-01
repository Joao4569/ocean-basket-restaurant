"""
Import models folder in order to create tables for our database
"""
from django.db import models
from django.contrib.auth.models import User


    # def __str__(self):
    # """This will modify the standard Django string method for
    # personalisation"""
    # return (f'{self.first_name} {self.last_name} table for '
    # f'{self.number_of_seats} on {self.date}')


class BookingInformation(models.Model):
    """
    Create a database model for storing online booking details
    """
    username = models.CharField(max_length=50)
    booking_title = models.CharField(max_length=50)
    number_of_seats = models.SmallIntegerField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    contact_number = models.CharField(max_length=12, null=False, blank=False)

    # Choices field for selection of lunch or dinner service
    LUNCH = 'LH'
    DINNER = 'DN'

    SERVICE_CHOICES = [
        (LUNCH, 'Lunch 13:00'),
        (DINNER, 'Dinner 19:00'),
    ]
    service = models.CharField(
        max_length=2,
        choices=SERVICE_CHOICES,
    )

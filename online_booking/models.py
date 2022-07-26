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
    date = models.DateField(null=False, blank=False)
    number_of_seats = models.SmallIntegerField(null=False, blank=False)

    def __str__(self):
        """This will modify the standard Django string method for
        personalisation"""
        return (f'{self.first_name} {self.last_name} table for '
                f'{self.number_of_seats} on {self.date}')

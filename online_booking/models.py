"""
Import models folder in order to create tables for our database
"""
from django.db import models


class BookingInformation(models.Model):
    """
    Create a database model for storing online booking details
    """
    # Choices field for selection of service taken from stackoverflow
    LUNCH = 'Lunch'
    DINNER = 'Dinner'

    SERVICE_CHOICES = [
        (LUNCH, 'Lunch 13:00'),
        (DINNER, 'Dinner 19:00'),
    ]
    service = models.CharField(
        max_length=6,
        choices=SERVICE_CHOICES,
    )
    username = models.CharField(max_length=150)
    booking_title = models.CharField(max_length=50)
    number_of_seats = models.SmallIntegerField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    # Contact number field recommendation taken from stackoverflow.com
    contact_number = models.CharField(max_length=12, null=False, blank=False)

    def __str__(self):
        """This will modify the standard Django string method for
        personalisation"""
        return (f'{self.booking_title} {self.contact_number} table for '
                f'{self.number_of_seats} on {self.date}')

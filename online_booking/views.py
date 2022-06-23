from django.shortcuts import render
from .models import CustomerBookingDetails

# Create your views here.


def get_home_page(request):
    """This function will display the home page"""
    bookings = CustomerBookingDetails.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'online_booking/index.html', context)

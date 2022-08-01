from django.shortcuts import render
from django.views import View
#from .forms import BookingForm
# from .models import CustomerDetails
from .models import BookingInformation

# Create your views here.


# def get_home_page(request):
# """This function will display the home page"""
# """bookings = CustomerBookingDetails.objects.all()
# context = {
# 'bookings': bookings
# }"""
# return render(request, 'online_booking/index.html')#, context)


class HomePage(View):
    """This function will display the home page"""
    def get(self, request):
        """This function will display the home page"""
        return render(request, "online_booking/index.html")


class RegisteredUser(View):

    def get(self, request):
        """This function will display the registration page"""
        bookings = BookingInformation.objects.all()
        context = {
                "bookings": bookings
            }
        return render(
            request,
            "online_booking/registered_user.html",
            context
        )

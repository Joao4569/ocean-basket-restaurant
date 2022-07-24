from django.shortcuts import render
from django.views import View
# from .models import CustomerBookingDetails

# Create your views here.


# def get_home_page(request):
# """This function will display the home page"""
# """bookings = CustomerBookingDetails.objects.all()
# context = {
# 'bookings': bookings
# }"""
# return render(request, 'online_booking/index.html')#, context)


"""This function will display the home page"""


class HomePage(View):

    def get(self, request):
        """This function will display the home page"""
        return render(request, "online_booking/index.html")


class RegistrationPage(View):

    def get(self, request):
        """This function will display the registration page"""
        return render(request, "online_booking/register.html")

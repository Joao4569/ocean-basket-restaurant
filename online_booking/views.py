from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import BookingForm
from .models import BookingInformation


class HomePage(View):
    """This function will display the home page"""
    def get(self, request):
        """This function will display the home page"""
        return render(request, "online_booking/index.html")


class CreateBooking(View):

    def get(self, request):
        """This function will display the registration page"""
        booking_form = {
                "booking_form": BookingForm()
            }

        return render(
            request,
            "online_booking/create_booking.html",
            booking_form
        )

    def post(self, request):
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking_form.instance.username = request.user.username
            booking_form.save()
        else:
            booking_form = BookingForm()

        bookings = BookingInformation.objects.all()
        context = {
            'bookings': bookings
        }

        return render(request,
            "online_booking/view_booking.html", context
        )


class ViewBooking(View):
    """This function will display the home page"""

    def get(self, request):
        """This function will display the home page"""
        bookings = BookingInformation.objects.all()
        context = {
            'bookings': bookings
        }
        return render(request, "online_booking/view_booking.html", context)


class EditBooking(View):
    """This function will display the edit booking page"""
    def get(self, request, booking_id):
        """This function will display the home page"""
        booking_id = get_object_or_404(BookingInformation, id=booking_id)
        edit_form = {
                "edit_form": BookingForm(instance=booking_id)
            }
        return render(request, "online_booking/edit_booking.html", edit_form)

    def post(self, request, booking_id):
        edit_form = BookingForm(data=request.POST)

        if edit_form.is_valid():
            edit_form.instance.username = request.user.username
            edit_form.instance.pk = booking_id
            edit_form.save()
        else:
            edit_form = BookingForm()

        bookings = BookingInformation.objects.all()
        context = {
            'bookings': bookings
        }

        return render(
            request,
            "online_booking/view_booking.html", context
        )

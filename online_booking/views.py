"""Import required object classes needed for views to function as intended
i.e. render views, get objects,get model and get form"""
from datetime import date
from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import BookingForm
from .models import BookingInformation


class HomePage(View):
    """This will display the home view"""
    def get(self, request):
        """This function will handle get requests for this view"""
        return render(request, "online_booking/index.html")


class CreateBooking(View):
    """This will display the create booking view"""
    def get(self, request):
        """This function will handle get requests for this view
        and allocate the form to render"""
        booking_form = {
                "booking_form": BookingForm()
            }

        return render(
            request,
            "online_booking/create_booking.html",
            booking_form
        )

    def post(self, request):
        """This function will handle post requests for this view, allocate
        which form to render, specify what to do if the form is valid and
        what information to send to the template as its context"""
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
    """This will display the view booking view"""

    def get(self, request):
        """This function will handle post requests for this view
        and what information to send to the template as its context"""
        bookings = BookingInformation.objects.all()
        context = {
            'bookings': bookings
        }
        return render(request, "online_booking/view_booking.html", context)


class EditBooking(View):
    """This will display the create booking view"""
    def get(self, request, booking_id):
        """This function will handle get requests for this view, allocate
        a booking entry identifier and allocate which form to render as
        well as allocate which entry to edit"""
        booking_identifier = get_object_or_404(BookingInformation,
                                               id=booking_id)
        edit_form = {
                "edit_form": BookingForm(instance=booking_identifier)
            }
        return render(request, "online_booking/edit_booking.html", edit_form)

    def post(self, request, booking_id):
        """This function will handle post requests for this view, allocate
        which form to render, specify what to do if the form is valid and
        what information to send to the template as its context"""
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


class DeleteBooking(View):
    """This view will allow the user to delete his booking"""
    def get(self, request, booking_id):
        """This function will handle get requests for this view, allocate
        a booking entry identifier, allocate which entry to delete and
        what information to send to the template"""
        booking_identifier = get_object_or_404(BookingInformation,
                                               id=booking_id)
        booking_identifier.delete()

        bookings = BookingInformation.objects.all()
        context = {
            'bookings': bookings
        }

        return render(
            request,
            "online_booking/view_booking.html", context
        )


class ViewBookingEmployee(View):
    """This function will display the home page"""

    def get(self, request):
        """This function will display the home page"""
        today = date.today()
        bookings = BookingInformation.objects.filter(date=today)
        context = {
            'bookings': bookings,
        }
        return render(request, "online_booking/view_booking.html", context)

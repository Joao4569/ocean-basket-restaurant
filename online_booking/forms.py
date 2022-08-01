from django import forms
from allauth.account.forms import SignupForm
from .models import BookingInformation


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=25, label='First Name')
    last_name = forms.CharField(
        max_length=25, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingInformation
        fields = ('booking_title', 'number_of_seats', 'contact_number', 'date',
                  'username')

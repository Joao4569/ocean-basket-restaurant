from django import forms
from datetime import datetime
from allauth.account.forms import SignupForm
from .models import BookingInformation



class CustomSignupForm(SignupForm):
    """This will add custom fields to the standard django
    allauth signup form - Taken from GeeksforGeeks.org
    credited in README.md"""
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


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingInformation
        fields = ('booking_title', 'number_of_seats',
                  'contact_number', 'date', 'service')
        widgets={
            'date': DateInput(),
            }


class DateForm(forms.Form):

    select_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date()}))

    class Meta:
        fields = ('select_date')

"""Import forms and model needed for creating forms"""
from django import forms
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
        """When saving allocate custom fields to model"""
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class DateInput(forms.DateInput):
    """This will set the input tape variable required for widget
    on theBookingForm"""
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """This will import the fields from the BookingForm model
    (method for creating date picker widget taken from
    stackoverflow - credited in readme"""
    class Meta:
        """This will set the Meta variables needed for the custom
        form to display as required"""
        model = BookingInformation
        fields = ('booking_title', 'number_of_seats',
                  'contact_number', 'date', 'service')
        widgets = {
            'date': DateInput(),
            }

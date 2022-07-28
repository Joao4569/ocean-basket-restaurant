from django import forms
from .models import CustomerDetails


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = ('first_name', 'last_name', 'contact_number', 'email',
                  'username', 'password',)

from django import forms
from .models import CustomerDetails


class Registration(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = ('first_name', 'last_name', 'contact_number', 'email',)

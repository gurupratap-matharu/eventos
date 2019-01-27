from django import forms
from .models import Event


class RegisterForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['event_description', 'event_date', 'event_time', 'event_country']

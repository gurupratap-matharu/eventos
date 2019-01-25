from django import forms

class RegisterForm(forms.Form):
    event_description = forms.CharField(label='Event', max_length=100)
    event_date = forms.DateTimeField(label='Event Date')
    event_time = forms.DateTimeField(label='Event Time')
    event_country = forms.CharField(label='Event Country', max_length=30)
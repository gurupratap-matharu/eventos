import pytz

from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Event, Country
from .forms import RegisterForm


def index(request):
    """
    Our index view function that allows to either list all events
    of register a new event.
    """
    return render(request, 'eventos/index.html')
    
def registerEvent(request):
    """
    Our view function to register an event in the database.
    """
    

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            event_description = form.cleaned_data['Event']
            event_date = form.cleaned_data['Event Date']
            event_time = form.cleaned_data['Event Time']
            event_country = form.cleaned_data['Event Country']
            print(event_description)
            print(event_date)
            print(event_country)

            Event.objects.create(event_description=event_description,event_date=event_date, event_time=event_time, event_country=event_country)
            
            event_list = Event.objects.all()
            context = {'event_list': event_list}
            return render(request, 'eventos/list.html', context)
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'eventos/form.html', {'form': form})
    
def listEvent(request):
    """
    The view function to list all the events in the database.
    """
    event_list = Event.objects.all()
    context = {'event_list': event_list}
    return render(request, 'eventos/list.html', context)
    

def detailEvent(request, event_id):
    """
    The view function that show the detail of each event like the
    date, time and country.
    """
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'eventos/detail.html', {'event': event})
    
def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'template.html', {'timezones': pytz.common_timezones})
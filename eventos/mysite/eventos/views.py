import pytz

from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from django.views import generic

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
            event_description = form.cleaned_data['event_description']
            event_date = form.cleaned_data['event_date']
            event_time = form.cleaned_data['event_time']
            event_country = form.cleaned_data['event_country']
            print(event_description)
            print(event_date)
            print(event_country)

            Event.objects.create(event_description=event_description, event_date=event_date, event_time=event_time, event_country=event_country)

            return HttpResponseRedirect(reverse('eventos:list'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'eventos/form.html', {'form': form})


class ListEvent(generic.ListView):
    """
    The view function to list all the events in the database.
    """
    template_name = 'eventos/list.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        """Return all the events registered so far."""
        return Event.objects.all()


class DetailEvent(generic.DetailView):
    """
    The view function that show the detail of each event like the
    date, time and country.
    """
    model = Event
    template_name = 'eventos/detail.html'


def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'template.html', {'timezones': pytz.common_timezones})

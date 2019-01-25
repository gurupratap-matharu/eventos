from django.contrib import admin

from .models import Event, Country
# Register your models here.
admin.site.register(Event)
admin.site.register(Country)
from django.utils import timezone
from django.db import models

# Create your models here.

class Country(models.Model):
    """
    Our Country models objects are created here and stored in the database
    as a table with the attributes mentioned below.
    """
    
    country_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.country_name

    
class Event(models.Model):
    """
    Our Event models objects are created here and stored in the database
    as a table with the attributes mentioned below.
    """

    event_description = models.CharField(max_length=200)
    event_date = models.DateTimeField('Event date')
    event_time = models.DateTimeField('Event time')
    event_country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_description


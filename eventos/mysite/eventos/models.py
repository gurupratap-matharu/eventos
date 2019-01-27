from django.utils import timezone
from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Country(models.Model):
    """
    Our Country models objects are created here and stored in the database
    as a table with the attributes mentioned below.
    """

    COUNTRY_CHOICES = (

        ('AR', 'Argentina'),
        ('AU', 'Australia'),
        ('AT', 'Austria'),
        ('BO', 'Bolivia'),
        ('BR', 'Brazil'),
        ('CA', 'Canada'),
        ('CL', 'Chile'),
        ('CN', 'China'),
        ('CO', 'Colombia'),
        ('IN', 'India'),
        ('ID', 'Indonesia'),
        ('MX', 'Mexico'),
        ('NL', 'Netherlands'),
        ('ZA', 'South Africa'),
        ('US', 'United States of America'),
        ('UY', 'Uruguay'),

    )
    country = models.CharField(
        max_length=2,
        choices=COUNTRY_CHOICES,
    )

    class Meta:
        ordering = ["country"]

    def __str__(self):
        return self.country


class Event(models.Model):
    """
    Our Event models objects are created here and stored in the database
    as a table with the attributes mentioned below.
    """

    event_description = models.CharField(max_length=200)
    event_date = models.DateField('Event date')
    event_time = models.TimeField('Event time')
    event_country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_description

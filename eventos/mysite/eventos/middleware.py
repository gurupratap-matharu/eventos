import pytz

from django.utils import timezone
from django.utils.timezone import get_current_timezone 
from django.utils.deprecation import MiddlewareMixin

class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
        """
        tz = get_current_timezone()
        timezone.activate(tz)


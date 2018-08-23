import warnings

from django.shortcuts import render
from django.utils import timezone

from .models import Event
import website.views


class IndexView(website.views.TemplateView):
    template_name = 'events/events.html'
    current_time = None

    def get(self, request, **kwargs):
        """
        Action to perform on a GET request. Fetches the published future and past events and displays them.
        """
        self.current_time = timezone.now()
        future_events = self.get_published_future_events()
        past_events = self.get_published_past_events()

        future_events_ordering = {
                'event_datetime_order': 'ascending',
                'publication_datetime_order': 'descending'
        }
        past_events_ordering = {
                'event_datetime_order': 'descending',
                'publication_datetime_order': 'descending'
        }

        ordered_future_events = self.order_events(future_events, **future_events_ordering)
        ordered_past_events = self.order_events(past_events, **past_events_ordering)

        context = {"past_events": ordered_past_events, "future_events": ordered_future_events}
        context.update(self.get_context_data())

        return render(request, self.template_name, context)

    def get_published_future_events(self):
        events = self.get_published_events()
        return events.filter(event_datetime__gte=self.current_time)

    def get_published_past_events(self):
        events = self.get_published_events()
        return events.filter(event_datetime__lt=timezone.now())

    def get_published_events(self):
        return Event.objects.exclude(publication_datetime__gte=self.current_time)

    def order_events(self, events, **kwargs):
        event_datetime_order = kwargs['event_datetime_order']
        publication_datetime_order = kwargs['publication_datetime_order']
        warning_strike_count = 0

        if event_datetime_order == 'ascending':
            events = events.order_by("+event_datetime")
        elif event_datetime_order == 'descending':
            events = events.order_by("-event_datetime")
        else:
            warning_strike_count += 1

        if publication_datetime_order == 'ascending':
            events = events.order_by("+publication_datetime")
        elif publication_datetime_order == 'descending':
            events = events.order_by("-publication_datetime")
        else:
            warning_strike_count += 1

        if warning_strike_count == 2:
            warnings.warn("Ordering of events not performed due to unrecognised orderings {} and {}".format(
                event_datetime_order, publication_datetime_order))

        return events

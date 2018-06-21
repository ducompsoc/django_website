from django.shortcuts import render

from .models import Event
import website.views


class IndexView(website.views.TemplateView):
    template_name = 'events/events.html'

    def get(self, request, **kwargs):
        """
        Action to perform on a GET request. Fetches the upcoming and past events and displays them.
        """
        events = Event.objects.order_by("-publication_datetime")
        context = {"events": events}
        context.update(self.get_context_data())

        return render(request, self.template_name, context)

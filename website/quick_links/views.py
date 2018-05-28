from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'quick_links/quick_links.html'

    def get(self, request, **kwargs):
        """
        Action to perform on a GET request. Renders the template given by template_name and returns it.
        """
        return render(request, self.template_name)

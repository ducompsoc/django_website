from django.shortcuts import render
from django.http import HttpResponse

import website.views


class IndexView(website.views.TemplateView):
    template_name = 'home/homepage.html'

    def get(self, request, **kwargs):
        """
        Action to perform on a GET request. Renders the template given by template_name and returns it.
        """
        return render(request, self.template_name, self.get_context_data())

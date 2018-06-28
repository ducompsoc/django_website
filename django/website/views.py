import django.views.generic
import datetime


class TemplateView(django.views.generic.TemplateView):
    """
    Defines a template view for all other views used in this site to extend.
    Sets as extra content to every page the current year.
    """
    extra_context = {'current_year': datetime.datetime.now().year}

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

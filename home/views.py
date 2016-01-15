from django.views.generic.base import TemplateView
from django.contrib.sites.models import Site

class home(TemplateView):

    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(home, self).get_context_data(**kwargs)
        context['site'] = Site.objects.get_current()
        return context
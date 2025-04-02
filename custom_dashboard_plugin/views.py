from django.views.generic import TemplateView

class WikiView(TemplateView):
    template_name = "custom_dashboard_plugin/wiki.html"
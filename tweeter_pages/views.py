from django.views.generic import TemplateView

class HomePageView(TemplateView):
    """View for the dashboard home page."""

    template_name = "home.html"
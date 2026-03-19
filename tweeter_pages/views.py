from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Twit

class HomePageView(ListView):
    """List view for the dashboard home page, containing a list of twits."""

    model = Twit
    template_name = "home.html"

class TwitDetailView(DetailView):
    """Detail view for a twit."""

    model = Twit
    template_name = "twits/twit_detail.html"

class TwitCreateView(CreateView):
    """Create view for a twit."""

    model = Twit
    template_name = "twits/twit_create.html"
    fields = (
        "body",
        "image_url",
    )

    def form_valid(self, form):
        """Sets the author of the twit to the logged in user."""
        
        form.instance.author = self.request.user
        return super().form_valid(form)

class TwitUpdateView(UpdateView):
    """Update view for a twit."""

    model = Twit
    template_name = "twits/twit_edit.html"
    fields = (
        "body",
        "image_url",
    )

class TwitDeleteView(DeleteView):
    """Delete view for a twit."""

    model = Twit
    template_name = "twits/twit_delete.html"
    success_url = reverse_lazy("home")
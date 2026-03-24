from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Twit

class HomePageView(ListView):
    """List view for the dashboard home page, containing a list of twits."""

    model = Twit
    template_name = "home.html"
    ordering = ["-created"]

class TwitDetailView(LoginRequiredMixin, DetailView):
    """Detail view for a twit."""

    model = Twit
    template_name = "twits/twit_detail.html"

class TwitCreateView(LoginRequiredMixin, CreateView):
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

class TwitUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update view for a twit."""

    model = Twit
    template_name = "twits/twit_edit.html"
    fields = (
        "body",
        "image_url",
    )

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TwitDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete view for a twit."""

    model = Twit
    template_name = "twits/twit_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
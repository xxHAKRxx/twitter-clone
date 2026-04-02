from urllib import request

from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .models import Twit
from .forms import CommentForm

class HomePageView(ListView):
    """List view for the dashboard home page, containing a list of twits."""

    model = Twit
    template_name = "home.html"
    # Orders each twit by when it was last updated, with most recent being first.
    ordering = ["-updated"]

class ProfileView(LoginRequiredMixin, ListView):
    """List view for a user's profile page, containing a list of their twits."""

    model = Twit
    template_name = "profile.html"
    ordering = ["-updated"]

class TwitDetailView(LoginRequiredMixin, View):
    """Detail view for a twit., which contains a form for comment creation."""

    def get(self, request, *args, **kwargs):
        """Performs a GET request to the view."""

        view = CommentGetView.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        """Performs a POST request to the view."""

        view = CommentPostView.as_view()
        return view(request, *args, **kwargs)

class CommentGetView(DetailView):
    """Gets the comment form for the twit detail view."""

    model = Twit
    template_name = "twits/twit_detail.html"

    def get_context_data(self, **kwargs):
        """Get the context data for the template."""

        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    
class CommentPostView(SingleObjectMixin, FormView):
    """View for posting comments onto a twit."""

    model = Twit
    form_class = CommentForm
    template_name = "twits/twit_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        """Creates a new comment if the form is valid."""

        comment = form.save(commit=False)
        comment.twit = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        """Redirects back to the detail view of the twit upon successfully posting a comment."""

        twit = self.get_object()
        return reverse("twit_detail", kwargs={"pk": twit.pk})

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
    
class TwitLikeView(LoginRequiredMixin, View):
    """View for liking a Twit."""

    def get(self, request, *args, **kwargs):
        # Get the data from the GET request
        twit_id = request.GET.get("twit_id", None)
        twit_action = request.GET.get("twit_action", None)

        twit = Twit.objects.get(id=twit_id)
        if twit_action == "like":
            twit.likes.add(request.user)
        else:
            twit.likes.remove(request.user)

        return JsonResponse({"success": True})
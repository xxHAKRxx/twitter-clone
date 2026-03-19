from django.urls import path
from .views import (
    HomePageView, 
    TwitDetailView,
    TwitCreateView,
    TwitUpdateView,
    TwitDeleteView,
)

urlpatterns = [
    path("twits/<int:pk>/", TwitDetailView.as_view(), name="twit_detail"),
    path("twits/<int:pk>/edit/", TwitUpdateView.as_view(), name="twit_edit"),
    path("twits/<int:pk>/delete/", TwitDeleteView.as_view(), name="twit_delete"),
    path("new_twit/", TwitCreateView.as_view(), name="twit_create"),
    path("", HomePageView.as_view(), name="home"),
]
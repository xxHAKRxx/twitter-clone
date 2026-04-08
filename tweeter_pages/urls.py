from django.urls import path
from .views import (
    HomePageView,
    ProfileView,
    ProfileEditView,
    TwitDetailView,
    TwitCreateView,
    TwitUpdateView,
    TwitDeleteView,
    TwitLikeView,
)

urlpatterns = [
    path("twits/<int:pk>/", TwitDetailView.as_view(), name="twit_detail"),
    path("twits/<int:pk>/edit/", TwitUpdateView.as_view(), name="twit_edit"),
    path("twits/<int:pk>/delete/", TwitDeleteView.as_view(), name="twit_delete"),
    path("twits/<int:pk>/like/", TwitLikeView.as_view(), name="twit_like"),
    path("new_twit/", TwitCreateView.as_view(), name="twit_create"),
    path("profile/<str:username>/", ProfileView.as_view(), name="profile"),
    path("profile/<str:username>/edit/", ProfileEditView.as_view(), name="profile_edit"),
    path("", HomePageView.as_view(), name="home"),
]
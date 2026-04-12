"""
Name: Evan Westcomb
Class: CIS 218
Date: 4/13/2026
"""

from django.urls import path
from .views import (
    ApiTwitListView,
    ApiTwitDetailView,
    ApiCommentListView,
    ApiCommentDetailView,
)

urlpatterns = [
    path("twits/", ApiTwitListView.as_view(), name="api_twit_list"),
    path("twits/<int:twit_pk>/", ApiTwitDetailView.as_view(), name="api_twit_detail"),
    path("twits/<int:twit_pk>/comments/", ApiCommentListView.as_view(), name="api_comment_list"),
    path("twits/<int:twit_pk>/comments/<int:comment_pk>/", ApiCommentDetailView.as_view(), name="api_comment_detail"),
]
"""
Name: Evan Westcomb
Class: CIS 218
Date: 4/13/2026
"""

from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
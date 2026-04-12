"""
Name: Evan Westcomb
Class: CIS 218
Date: 4/13/2026
"""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Modifies the default user creation form to include the date of birth field."""

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
            "date_of_birth",
        )

class CustomUserChangeForm(UserChangeForm):
    """Modifies the default user edit form to include the date of birth field."""

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "date_of_birth",
        )
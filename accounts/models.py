"""
Name: Evan Westcomb
Class: CIS 218
Date: 4/13/2026
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """A custom user model that adds extra fields to the default user model."""

    date_of_birth = models.DateField(null=True, blank=True)
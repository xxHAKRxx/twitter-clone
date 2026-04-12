"""
Name: Evan Westcomb
Class: CIS 218
Date: 4/13/2026
"""

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """A form for creating a comment on a twit."""

    class Meta:
        model = Comment
        fields = ("body",)
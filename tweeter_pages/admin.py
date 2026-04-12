"""
Name: Evan Westcomb
Class: CIS 218
Date: 4/13/2026
"""

from django.contrib import admin
from .models import Twit, Comment

class CommentInline(admin.TabularInline):
    """Inline for seeing comments on a twit in the admin page."""

    model = Comment


class TwitAdmin(admin.ModelAdmin):
    """Custom admin page for twits, which shows all of the comments for a twit."""

    inlines = [
        CommentInline,
    ]


admin.site.register(Twit, TwitAdmin)
admin.site.register(Comment)
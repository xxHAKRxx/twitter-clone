from django.db import models
from django.conf import settings
from django.urls import reverse

class Twit(models.Model):
    """
    The model for a twit.

    Attributes:
    - author (int NOT NULL): The user that created the twit.
    - body (longtext): The text content of the twit.
    - image_url (varchar(400)): The URL of any images attached to the twit.
    - created (datetime AUTO): The date and time the twit was created.
    - updated (datetime AUTO): The date and time the twit was last updated.
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    body = models.TextField(blank=True)
    image_url = models.URLField(blank=True, max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Twit as a string"""
        
        return str(self.author)
    
    def get_absolute_url(self):
        return reverse("twit_detail", kwargs={"pk": self.pk})
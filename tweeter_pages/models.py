from django.db import models
from django.conf import settings
from django.urls import reverse

class Twit(models.Model):
    """
    The model for a twit.

    Attributes:
    - author (int NOT NULL): The user that created the twit.
    - likes (ManyToMany): The users that have liked the twit.
    - body (longtext): The text content of the twit.
    - image_url (varchar(400)): The URL of any images attached to the twit.
    - created (datetime AUTO): The date and time the twit was created.
    - updated (datetime AUTO): The date and time the twit was last updated.
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="twits",
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_twits",
        blank=True,
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
    
    def get_like_url(self):
        """Get the like URL based on the twit's PK."""
        
        return reverse("twit_like", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    """
    The model for a comment on a twit.

    Attributes:
    - twit (int NOT NULL): The twit that the comment is on.
    - author (int NOT NULL): The user that created the comment.
    - body (varchar(140)): The content of the comment.
    - created (datetime AUTO): The date and time the comment was created.
    - updated (datetime AUTO): The date and time the comment was last updated.
    """
    twit = models.ForeignKey(
        Twit,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    body = models.CharField(blank=True, max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Comment as a string"""
        
        return str(self.author)
    
    def get_absolute_url(self):
        return reverse("twit_detail")
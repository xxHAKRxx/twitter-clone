from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import JsonResponse
from tweeter_pages.models import Twit, Comment

class ApiTwitListView(LoginRequiredMixin, View):
    """List of all twits as a JSON."""

    def get(self, request, *args, **kwargs):
        twits = list(Twit.objects.values())
        
        return JsonResponse(twits, safe=False)
    
class ApiTwitDetailView(LoginRequiredMixin, View):
    """Detail view for a twit as a JSON, showing all comments on it."""

    def get(self, request, twit_pk, *args, **kwargs):
        twit = Twit.objects.values().get(
            pk=twit_pk,
        )
        comments = list(
            Comment.objects.filter(
                twit__pk=twit_pk,
            ).values()
        )
        
        twit["comments"] = comments
        return JsonResponse(twit, safe=False)
    
class ApiCommentListView(LoginRequiredMixin, View):
    """List of all comments as a JSON."""

    def get(self, request, twit_pk, *args, **kwargs):
        comments = list(
            Comment.objects.filter(
                twit__pk=twit_pk,
            ).values()
        )

        return JsonResponse(comments, safe=False)
    
class ApiCommentDetailView(LoginRequiredMixin, View):
    """Detail view for a comment as a JSON."""

    def get(self, request, twit_pk, comment_pk, *args, **kwargs):
        comment = Comment.objects.values().get(
            pk=comment_pk,
        )

        return JsonResponse(comment, safe=False)
from django.utils.timezone import now
from .models import SNUser


class SetLastVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            SNUser.objects.filter(pk=request.user.pk).update(last_request_time=now())
        return response

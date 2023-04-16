from rest_framework.response import Response

from core.models import Post
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from users.models import SNUser
from django.db.models import Count
from django.db.models.functions import TruncDay


class UserAnalytics(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(SNUser, pk=user_id)
        return Response(
            status=200,
            data={
                "last_login": user.last_login,
                "last_request": user.last_request_time,
            },
        )


class DailyAnalytics(APIView):
    def get(self, request, date_from, date_to):
        posts_analytics = (
            Post.objects.filter(created_at__range=(date_from, date_to))
            .annotate(date=TruncDay("created_at"))
            .values("date")
            .annotate(created_count=Count("id"))
            .order_by("-date")
        )
        return Response(status=200, data=posts_analytics)

from django.urls import include, path
from .views import DailyAnalytics, UserAnalytics

urlpatterns = [
    path("<int:user_id>/", UserAnalytics.as_view()),
    path("date_from=<str:date_from>&date_to=<str:date_to>/", DailyAnalytics.as_view()),
]

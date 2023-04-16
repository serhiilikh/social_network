from django.urls import include, path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="Social Network API",
        default_version="v1",
        description="",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", include("core.urls")),
    path("users/", include("users.urls")),
    path("analytics/", include("analytics.urls")),
    path("auth/", include("djoser.urls.jwt")),
]

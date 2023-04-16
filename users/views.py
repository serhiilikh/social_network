from rest_framework import status
from rest_framework.response import Response


from djoser.views import UserViewSet


class UsersViewSet(UserViewSet):
    http_method_names = ["get", "post", "patch", "delete", "head"]

    def list(self, request, *args, **kwargs):
        ...

    def activation(self, request, *args, **kwargs):
        ...

    def resend_activation(self, request, *args, **kwargs):
        ...

    def set_username(self, request, *args, **kwargs):
        ...

    def reset_username_confirm(self, request, *args, **kwargs):
        ...

    def reset_username(self, request, *args, **kwargs):
        ...

    def reset_password_confirm(self, request, *args, **kwargs):
        ...

    def reset_password(self, request, *args, **kwargs):
        ...

    def set_password(self, request, *args, **kwargs):
        ...

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

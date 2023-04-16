from django.contrib.auth.models import AbstractUser
from django.db.models import DateTimeField
from django.utils import timezone


class SNUser(AbstractUser):
    last_request_time = DateTimeField(default=timezone.now)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        db_table = "auth_user"

    def __str__(self):
        if self.email:
            return self.email
        return str(self.id)

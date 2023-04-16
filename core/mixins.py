from django.db import models
from django.utils import timezone


class AutoLogMixin(models.Model):
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(editable=False, default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.pk and not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True

from django.db import models

from users.models import SNUser
from core.mixins import AutoLogMixin


class Post(AutoLogMixin):
    author = models.ForeignKey(SNUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Upvote(AutoLogMixin):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(SNUser, on_delete=models.CASCADE)

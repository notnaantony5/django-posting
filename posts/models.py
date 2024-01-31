from django.db import models

from core.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
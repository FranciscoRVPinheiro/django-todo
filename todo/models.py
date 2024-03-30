from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.conf import settings

class User(AbstractUser):
    pass

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.title}' 
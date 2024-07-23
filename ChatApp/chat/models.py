# chat/models.py

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class UserStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_activity = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    def is_online(self):
        now = timezone.now()
        if self.last_activity and (now - self.last_activity).seconds < 300:  # 5 minutes
            return True
        return False

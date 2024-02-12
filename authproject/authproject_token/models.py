from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Token(models.Model):
    referor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="token_referor")
    referree = models.ForeignKey(User, on_delete=models.CASCADE, related_name="token_referree")
    
    token = models.CharField(max_length=32)
    active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    live_time = models.IntegerField(default=15)
    
    def token_is_alive(self):
        now = timezone.now()
        is_alive = now - self.create_date < timedelta(minutes=self.live_time)
        return is_alive
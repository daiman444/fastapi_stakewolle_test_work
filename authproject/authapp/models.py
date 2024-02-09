from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    user_name = models.CharField(
        max_length=16
    )
    email = models.EmailField(
        verbose_name="Input yor e-mail",
        unique=True,
        default='xxx@yyy.zzz'
    )
    date_registration = models.DateTimeField(
        'date of registration', 
        default=timezone.now
    )
    
    
class Token(models.Model):
    referrer = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name="tokens",
        default=None,
    )
    referee = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="referee_user",
        null=True, default=None,
        blank=True,
    )
    token = models.IntegerField(
        unique=True, 
        default=0,
    )
    token_status = models.BooleanField(
        default=True,
    )
    date_creation = models.DateTimeField(
        'date of creation', 
        default=timezone.now,
    )
    
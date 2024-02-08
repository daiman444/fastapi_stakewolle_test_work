from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=16)
    email = models.EmailField(unique=True, default='None')
    date_registration = models.DateTimeField('date of registration', default=timezone.now)
    
    
    def __str__(self) -> str:
        return self.user_name
    
    
class Token(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.IntegerField(unique=True, default=0)
    date_creation = models.DateTimeField('date of creation', default=timezone.now)
    
    def __str__(self) -> str:
        return self.owner
    
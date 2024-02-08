from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=16)
    email = models.EmailField(default='None')
    token = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.user_name
    
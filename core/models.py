from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=200)


class Account(models.Model):
    user_name= models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.FloatField()

    def __str__(self):
        return self.name
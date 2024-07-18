from django.db import models

# Create your models here.
class user_information(models.Model):
    name  =models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Age = models.IntegerField(default=0)
    gender = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
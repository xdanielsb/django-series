from django.db import models

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=10)
    age = models.IntegerField()
    rescue_date = models.DateField()
    

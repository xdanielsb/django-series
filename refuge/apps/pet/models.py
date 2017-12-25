from django.db import models

# Create your models here.
from apps.adoption.models import Person

class Vaccine(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return "{}".format(self.name)

class Pet(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=10)
    age = models.IntegerField()
    rescue_date = models.DateField()
    owner = models.ForeignKey(Person, null = True, blank = True, on_delete=models.CASCADE)
    vaccines = models.ManyToManyField(Vaccine, blank = True)

    def __str__(self):
        return "{}".format(self.name)

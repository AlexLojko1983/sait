from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)

# Create your models here.

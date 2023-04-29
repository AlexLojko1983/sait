from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    name = models.CharField(max_length=20)

    CHOICES =(
        ("M", "Man"),
        ("W", "Women"),
    )

    age = models.IntegerField()
    email = models.EmailField(max_length=50, primary_key=True)
    password = models.CharField(max_length=20)
    gender = models.CharField(choices=CHOICES, default="M")
    pasrepeat = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Create your models here.

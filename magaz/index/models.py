from django.db import models


class Person(models.Model):

    CHOICES =(
        ("M", "Man"),
        ("W", "Women"),
    )

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    gender = models.CharField(choices=CHOICES)

# Create your models here.

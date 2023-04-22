from django.db import models


class Person(models.Model):

    CHOICES =(
        ("M", "Man"),
        ("W", "Women"),
    )
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=50, primary_key=True)
    password = models.CharField(max_length=20)
    gender = models.CharField(choices=CHOICES, default="M")

# Create your models here.
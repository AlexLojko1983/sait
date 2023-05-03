from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    prise = models.DecimalField(max_digits=7, decimal_places=2)
    # img = models.ImageField()
    unit = models.CharField(max_length=2)

    def __str__(self):
        return self.name
# Create your models here.

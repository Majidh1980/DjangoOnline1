from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

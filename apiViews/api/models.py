from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    name = models.ManyToManyField(Product)
    total_cost = models.IntegerField()

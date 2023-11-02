from typing import Any
from django.db import models
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=400)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = "PE"  # pending shipping number
        APPROVED = "AP"  # got shipping number
        FULFILLED = "FU"  # shipping number is delivered
    
    status = models.CharField(
        max_length=2,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )
    complete = models.BooleanField(default=False)
    order_lines = models.ManyToManyField(Product, through="Orderline")
    date = models.DateTimeField(default=timezone.now)
    shipping_number = models.IntegerField(blank=True, null=True, db_index=True)


class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    

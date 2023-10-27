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
        PENDING = "PE"
        APPROVED = "AP"
        FULFILLED = "FU"
    
    status = models.CharField(
        max_length=2,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )
    complete = models.BooleanField(default=False)
    order_lines = models.ManyToManyField(Product, through="Orderline")
    date = models.DateTimeField(default=timezone.now)


class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    

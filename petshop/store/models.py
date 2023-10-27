from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=400)
    quantity = models.IntegerField()

# class Order(models.Model):
#     # only order 1 thing for now
    

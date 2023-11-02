from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from rest_framework import viewsets
from .serializers import ProductSerializer, OrderSerializer

from .models import Product, Order, OrderLine


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class IndexView(generic.ListView):
    model = Product


class DetailView(generic.DetailView):
    model = Product
    template_name = "store/detail.html"


# lets say you can only buy one product at one time
def submitOrder(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order = Order()
    order.save()
    order.order_lines.add(product, through_defaults={"quantity": request.POST["quantity"]})
    return HttpResponseRedirect(reverse("store:index"))



def completeOrder(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.shipping_number = request.POST["shipping_number"]
    order.OrderStatus = Order.OrderStatus.FULFILLED



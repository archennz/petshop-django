from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Product, Order, OrderLine


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
    
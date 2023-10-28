from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Product


class IndexView(generic.ListView):
    template_name = "store/index.html"
    context_object_name = "products"

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.get_queryset()


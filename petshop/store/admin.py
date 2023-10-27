from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "quantity"]
    search_fields = ["name"]


class OrderLineInline(admin.TabularInline):
    model = Order.order_lines.through
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ["status", "complete"]
    list_display = ["id", "status", "date", "complete"]
    inlines = [
        OrderLineInline
    ]

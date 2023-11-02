from rest_framework import serializers
from .models import Product, Order, OrderLine


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity')


class OrderLineSerializer(serializers.Serializer):
    # need to serialize product name and not get into N+1 issues
    quantity = serializers.IntegerField()


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(Order.OrderStatus)
    order_lines = OrderLineSerializer(many=True)

    class Meta:
        model = Order
        # add order lines
        fields = ('id', 'complete', 'date', 'shipping_number', 'status', 'order_lines')
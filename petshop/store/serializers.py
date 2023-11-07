from rest_framework import serializers
from .models import Product, Order, OrderLine


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity')

class OrderLineSerializer(serializers.ModelSerializer):
    # TODO: investigate N+1 issues
    product_id = serializers.IntegerField(source='product.id')
    name = serializers.ReadOnlyField(source='product.name')
    
    class Meta:
        model = OrderLine
        fields = ('quantity', 'product_id', 'name')

class OrderSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(Order.OrderStatus)
    order_lines = OrderLineSerializer(source='orderline_set' , many=True)

    class Meta:
        model = Order
        fields = ('id', 'complete', 'date', 'shipping_number', 'status', 'order_lines')

    
    def create(self, validated_data):
        orderlines = validated_data.pop('orderline_set')
        # just save the order first
        order = Order.objects.create(**validated_data)
        order.save()
        for orderline in orderlines:
            product = Product.objects.get(pk=orderline['product']['id'])
            order.order_lines.add(product, through_defaults={'quantity': orderline['quantity']})
        return order

class ShippingNumberSerializer(serializers.Serializer):
    shipping_number = serializers.IntegerField()
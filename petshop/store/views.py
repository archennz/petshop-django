from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ProductSerializer, OrderSerializer

from .models import Product, Order

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
    @action(detail=True, methods=['POST'])
    def complete_order(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.shipping_number = request.data["shipping_number"]
        order.OrderStatus = Order.OrderStatus.FULFILLED
        return Response()



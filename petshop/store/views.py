from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ProductSerializer, OrderSerializer, ShippingNumberSerializer

from .models import Product, Order

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
    @action(detail=True, methods=['post'])
    def complete_order(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = ShippingNumberSerializer(data=request.data)
        if serializer.is_valid():            
            order.update_shipping(request.data["shipping_number"])
            order.save()
            return Response()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



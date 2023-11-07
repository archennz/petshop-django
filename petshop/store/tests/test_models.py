import unittest
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from ..models import Order

class TestOrder(unittest.TestCase):
    
    def test_correctly_updates_shipping(self):
        order = self.create_order()
        new_number = 1234
        order.update_shipping(new_number)
        self.assertEqual(order.shipping_number, new_number)
        self.assertEqual(order.status, Order.OrderStatus.FULFILLED.value)
        

    def create_order(
            status = "PE", 
            complete = False, 
            date = timezone.now(), 
            shipping_number = None
            ):
        return Order(
            status = status,
            complete = complete,
            date = date,
            shipping_number = shipping_number
        )


class Test_E2E(APITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        Order.objects.create()
        return super().setUpClass()

    def test_get_orders(self):
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    
    def test_update_shipping_with_bad_data_returns_bad_request(self):
        response = self.client.post('/api/orders/1/complete_order/', data={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_update_shipping_with_bad_data_returns_bad_request(self):
        response = self.client.post('/api/orders/1/complete_order/', data={'shipping_number': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

import unittest
from django.utils import timezone
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
import unittest
from unittest.mock import patch
from modules.delivery import Delivery
from modules.cooking import Margherita


class TestDelivery(unittest.TestCase):
    def test_delivery_instance(self):
        self.assertEqual(
            Delivery(True, Margherita('L')).pizza_name, 'Margherita'
        )

    @patch('builtins.print')
    def test_delivery_by_courier(self, mock_print):
        pizza_instance = Delivery(True, Margherita('L'))
        pizza_instance.courier.__wrapped__(pizza_instance)
        mock_print.assert_called_with(
            f'{pizza_instance.pizza_emoji} {pizza_instance.pizza_name} '
            f'({pizza_instance.pizza_size}) is about to be '
            'delivered!'
        )

    @patch('builtins.print')
    def test_delivery_by_client(self, mock_print):
        pizza_instance = Delivery(False, Margherita('L'))
        pizza_instance.client_taking.__wrapped__(pizza_instance)
        mock_print.assert_called_with(
            f'{pizza_instance.pizza_emoji} {pizza_instance.pizza_name} '
            f'({pizza_instance.pizza_size}) is about to be '
            'picked up by client!'
        )


if __name__ == '__main__':
    unittest.main()

from typing import Type
from cooking import Pizza


class Delivery:
    def __init__(self, delivery: bool, pizza: Type[Pizza]):
        self.delivery_status = delivery
        self.pizza_name = pizza.name
        self.pizza_size = pizza.size

    def get_pizza(self):
        if self.delivery_status:
            print(f'{self.pizza_name} ({self.pizza_size}) '
                  'is about to be delivered!')
        else:
            print(f'{self.pizza_name} ({self.pizza_size}) '
                  'is about to be picked up by client!')

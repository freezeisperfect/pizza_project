from typing import Type
from cooking import Pizza
from log import log


class Delivery:
    def __init__(self, delivery: bool, pizza: Type[Pizza]):
        self.delivery_status = delivery
        self.pizza_name = pizza.name
        self.pizza_size = pizza.size
        self.pizza_emoji = pizza.emoji

    def get_pizza(self):
        if self.delivery_status:
            self.courier()
        else:
            self.client_taking()

    @log('🏍️ Delivered in {} sec!')
    def courier(self):
        print(f'{self.pizza_emoji} {self.pizza_name} ({self.pizza_size}) '
              'is about to be delivered!')

    @log('👜 Took in {} sec!')
    def client_taking(self):
        print(f'{self.pizza_emoji} {self.pizza_name} ({self.pizza_size}) '
              'is about to be picked up by client!')

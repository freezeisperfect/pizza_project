from typing import Type
from modules.cooking import Pizza
from modules.log import log


class Delivery:
    """
    Класс, характеризующий доставку пиццы.

    Class attributes
    ----------------
    delivery_status: bool
        Флаг доставки, если выставлен как True, то доставка осуществляется
        курьеров, иначе - самовывоз.
    pizza_name: str
        Название пиццы.
    pizza_size: str
        Размер пиццы.
    pizza_emoji: str
        Эмодзи для отображения пиццы.

    Methods
    -------
    __init__(self, delivery: bool, pizza: Type[Pizza]) -> None:
        Инициализирует новый инстанс службы доставки.
    get_pizza(self) -> None:
        Метод, определяющий способ доставки пиццы.
    courier(self) -> None:
        Метод доставки пиццы курьером.
    client_taking(self) -> None:
        Метод доставки пиццы самовывозом.
    """
    def __init__(self, delivery: bool, pizza: Type[Pizza]) -> None:
        """
        Инициализирует новый инстанс службы доставки.

        Parameters
        ----------
        delivery: bool
            Флаг доставки, если выставлен как True, то доставка осуществляется
            курьеров, иначе - самовывоз.
        pizza: Type[Pizza]
            Инстанс пиццы для определения ее параметров.
        """
        self.delivery_status = delivery
        self.pizza_name = pizza.name
        self.pizza_size = pizza.size
        self.pizza_emoji = pizza.emoji

    def get_pizza(self) -> None:
        """
        Метод, определяющий способ доставки пиццы.
        """
        if self.delivery_status:
            self.courier()
        else:
            self.client_taking()

    @log('🏍️ Delivered in {} sec!')
    def courier(self) -> None:
        """
        Метод доставки пиццы курьером.
        """
        print(f'{self.pizza_emoji} {self.pizza_name} ({self.pizza_size}) '
              'is about to be delivered!')

    @log('👜 Took in {} sec!')
    def client_taking(self) -> None:
        """
        Метод доставки пиццы самовывозом.
        """
        print(f'{self.pizza_emoji} {self.pizza_name} ({self.pizza_size}) '
              'is about to be picked up by client!')

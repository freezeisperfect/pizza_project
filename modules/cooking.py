class Pizza:
    actual_pizza_sizes = ['L', 'XL']

    def __init__(self, pizza_size: str = 'L') -> None:
        if not isinstance(pizza_size, str):
            raise ValueError
        if pizza_size not in self.actual_pizza_sizes:
            raise TypeError

        self.receipt = None
        self.size = pizza_size

    def dict(self) -> dict[str, list[str]]:
        pizza_name = self.__class__.__name__
        return {pizza_name: self.receipt}


class Margherita(Pizza):
    def __init__(self, pizza_size):
        super().__init__(pizza_size)
        self.receipt = ['tomato sauce', 'mozzarella', 'tomatoes']


class Pepperoni(Pizza):
    def __init__(self, pizza_size):
        super().__init__(pizza_size)
        self.receipt = ['tomato sauce', 'mozzarella', 'pepperoni']


class Hawaiian(Pizza):
    def __init__(self, pizza_size):
        super().__init__(pizza_size)
        self.receipt = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']


if __name__ == '__main__':
    my_pizza = Margherita('XL')
    print(my_pizza.dict())

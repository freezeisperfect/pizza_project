import inspect
from log import log


class Pizza:
    actual_pizza_sizes = ['L', 'XL']

    def __init__(self, pizza_size: str = 'XL', emoji: str = '🤔') -> None:
        if not isinstance(pizza_size, str) or not isinstance(emoji, str):
            raise ValueError
        if pizza_size not in self.actual_pizza_sizes:
            raise TypeError

        self.receipt = None
        self.size = pizza_size
        self.name = str(self)
        self.emoji = emoji

    def __str__(self) -> str:
        return self.__class__.__name__

    def __eq__(self, other) -> bool:
        if not isinstance(other, Pizza):
            raise ValueError
        return self.name == other.name \
            and self.size == other.size \
            and set(self.receipt) == set(other.receipt)

    @log('💨 Cooked in {} sec!')
    def cook(self) -> None:
        print(f'🥵 LET HIM COOK! (◕‿◕) {self.name} {self.emoji} is cooking!')

    def dict(self) -> dict[str, list[str]]:
        return {self.name: self.receipt}


class Margherita(Pizza):
    def __init__(self, pizza_size: str = 'XL', emoji: str = '🧀'):
        super().__init__(pizza_size, emoji)
        self.receipt = ['tomato sauce', 'mozzarella', 'tomatoes']


class Pepperoni(Pizza):
    def __init__(self, pizza_size: str = 'XL', emoji: str = '🍕'):
        super().__init__(pizza_size, emoji)
        self.receipt = ['tomato sauce', 'mozzarella', 'pepperoni']


class Hawaiian(Pizza):
    def __init__(self, pizza_size: str = 'XL', emoji: str = '🍍'):
        super().__init__(pizza_size, emoji)
        self.receipt = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']


def get_pizzas():
    current_module = inspect.getmodule(inspect.currentframe())
    classes = {
        name.lower(): cls for name, cls in inspect.getmembers(current_module)
        if inspect.isclass(cls) and name != 'Pizza'
    }
    return classes


if __name__ == '__main__':
    my_pizza = Margherita()
    print(my_pizza.dict())
    my_pizza.cook()
    print(my_pizza.name)

    my_margherita = Margherita()
    print(my_margherita == my_pizza)

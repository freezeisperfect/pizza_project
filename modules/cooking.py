import inspect
from modules.log import log
from typing import Type


class Pizza:
    """
    Класс, характеризующий пиццу.

    Attributes
    ----------
    actual_pizza_sizes: list
        Доступные размеры пиццы в виде списка.

    Class attributes
    ----------------
    receipt: list[str]
        Рецепт пиццы, представленный в виде списка, где ключом является
        название пиццы, а значением - список из ингридиентов для пиццы.
        В классе Pizza для абстрактной пиццы инициализирован как None.
    size: str
        Размер пиццы из списка доступных к заказу в виде строки.
        По умолчанию равен 'XL'.
    emoji: str
        Эмодзи для отображения при заказе пиццы.
        По умолчанию '🤔'.

    Methods
    -------
    __init__(self, size: str = 'XL', emoji: str = '🤔') -> None:
        Инициализирует новый инстанс пиццы.
    __str__(self) -> str:
        Возвращает название пиццы в виде строки. Для отображения названия
        используется название класса.
    __eq__(self, other) -> bool:
        Сравнивает две пиццы на равенство значений инстансов.
    cook(self) -> None:
        Метод приготовления пиццы. Выполняется декорированная функция,
        которая печатает логированное время приготовления пиццы.
    dict(self) -> dict[str, list[str]]:
        Возвращает рецепт пиццы в виде словаря, где ключ - название пиццы,
        значение - ее рецепт в виде списка.
    """
    actual_pizza_sizes = ['L', 'XL']

    def __init__(self, size: str = 'XL', emoji: str = '🤔') -> None:
        """
        Инициализирует новый инстанс пиццы.

        Parameters
        ----------
        size: str
            Размер пиццы, по умолчанию равен 'XL'.
        emoji: str
            Эмодзи, характеризующий пиццу. По умолчанию равен '🤔'.
        """
        if not isinstance(size, str) or not isinstance(emoji, str):
            raise ValueError
        if size not in self.actual_pizza_sizes:
            raise TypeError

        self.receipt = []
        self.size = size
        self.name = str(self)
        self.emoji = emoji

    def __str__(self) -> str:
        """
        Возвращает название пиццы в виде строки. Для отображения названия
        используется название класса.

        Returns
        -------
        str
            Название пиццы в виде строки.
        """
        return self.__class__.__name__

    def __eq__(self, other) -> bool:
        """
        Сравнивает две пиццы на равенство значений инстансов.

        Parameters
        ----------
        other: Pizza
            Инстанс класса Pizza для сравнения.

        Returns
        -------
        bool
            Возвращает True, если пиццы эквивалентны друг другу, иначе - False.
        """
        if not isinstance(other, Pizza) or self.receipt is None:
            raise ValueError
        return self.name == other.name \
            and self.size == other.size \
            and set(self.receipt) == set(other.receipt)

    @log('💨 Cooked in {} sec!')
    def cook(self) -> None:
        """
        Метод приготовления пиццы. Выполняется декорированная функция,
        которая печатает логированное время приготовления пиццы.
        """
        print(f'🥵 LET HIM COOK! (◕‿◕) {self.name} {self.emoji} is cooking!')

    def dict(self) -> dict[str, list[str]]:
        """
        Возвращает рецепт пиццы в виде словаря, где ключ - название пиццы,
        значение - ее рецепт в виде списка.

        Returns
        -------
        dict[str, list[str]]
            Словарь вида название пиццы: рецепт пиццы.
        """
        return {self.name: self.receipt}


class Margherita(Pizza):
    """
    Класс, создающий пиццу Margherita.
    """
    def __init__(self, pizza_size: str = 'XL', emoji: str = '🧀'):
        super().__init__(pizza_size, emoji)
        self.receipt = ['tomato sauce', 'mozzarella', 'tomatoes']


class Pepperoni(Pizza):
    """
    Класс, создающий пиццу Pepperoni.
    """
    def __init__(self, pizza_size: str = 'XL', emoji: str = '🍕'):
        super().__init__(pizza_size, emoji)
        self.receipt = ['tomato sauce', 'mozzarella', 'pepperoni']


class Hawaiian(Pizza):
    """
    Класс, создающий пиццу Hawaiian.
    """
    def __init__(self, pizza_size: str = 'XL', emoji: str = '🍍'):
        super().__init__(pizza_size, emoji)
        self.receipt = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']


def get_pizzas() -> dict[str, Type]:
    """
    Получает классы пицц, определенные в модуле (кроме класса-родителя Pizza).

    Returns
    -------
    dict[str, Type]
        Словарь вида название пиццы (приведенное к нижнему регистру):
        объект класса для данной пиццы.
    """
    current_module = inspect.getmodule(inspect.currentframe())
    classes = {
        name.lower(): cls for name, cls in inspect.getmembers(current_module)
        if inspect.isclass(cls) and name != 'Pizza'
    }
    return classes


if __name__ == '__main__':  # pragma: no cover
    pizza = Pizza()
    print(str(pizza))
    my_pizza = Margherita()
    print(my_pizza.dict())
    my_pizza.cook()
    print(my_pizza.name)

    my_margherita = Margherita()
    print(my_margherita == my_pizza)

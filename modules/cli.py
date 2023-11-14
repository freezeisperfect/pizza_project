import click
from modules.cooking import get_pizzas
from modules.delivery import Delivery


ACTUAL_PIZZAS = get_pizzas()


@click.group
def cli():
    """
    CLI-интерфейс для заказа пиццы (order) и вывода меню (menu).
    """
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--size', default='XL')
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool, size: str) -> None:
    """
    Выполнение заказа пиццы с опцией выбора доставки (или самовывоза при
    ее отсуствтвии), а также размера пиццы.

    Parameters
    ----------
    pizza: str
        Название пиццы для заказа, передается как аргумент при вызове order.
    delivery: bool
        Флаг доставки, если True - то заказ будет доставлен, иначе - заказ
        для самовывоза. Задается флагом --delivery при вызове order.
    size: str
        Размер пиццы для заказа. Задается как опциональный аргумент с помощью
        флага --size при вызове order.

    Returns
    -------
    None

    Usage
    -----
    $ python cli.py order --delivery --size L Margherita
    $ python cli.py menu
    """
    if not isinstance(pizza, str) or not isinstance(size, str):
        raise ValueError
    if pizza.lower() not in ACTUAL_PIZZAS.keys():
        raise TypeError

    pizza_object = ACTUAL_PIZZAS[pizza.lower()](size)
    pizza_object.cook()

    Delivery(delivery, pizza_object).get_pizza()


@cli.command()
def menu() -> None:
    """
    Вывод меню пицц для заказа с ингридиентами для ее изготовления.

    Returns
    -------
    None

    Usage
    -----
    $ python cli.py menu
    """
    for name, pizza in ACTUAL_PIZZAS.items():
        pizza_item = pizza()
        click.echo(
            f'- {pizza_item.name} {pizza_item.emoji}: ' +
            ', '.join(pizza_item.receipt)
        )


if __name__ == '__main__':
    cli()

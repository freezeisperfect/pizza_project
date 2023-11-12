import click
from cooking import get_pizzas
from delivery import Delivery


@click.group
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--size', default='XL')
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool, size: str):
    actual_pizzas = get_pizzas()
    if not isinstance(pizza, str):
        raise ValueError
    if pizza.lower() not in actual_pizzas.keys():
        raise TypeError

    pizza_object = actual_pizzas[pizza.lower()](size)
    pizza_object.cook()

    Delivery(delivery, pizza_object).get_pizza()


if __name__ == '__main__':
    cli()

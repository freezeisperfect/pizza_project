import click
from cooking import get_pizzas
from delivery import Delivery


ACTUAL_PIZZAS = get_pizzas()


@click.group
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--size', default='XL')
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool, size: str):

    print(ACTUAL_PIZZAS)
    if not isinstance(pizza, str) or not isinstance(size, str):
        raise ValueError
    if pizza.lower() not in ACTUAL_PIZZAS.keys():
        raise TypeError

    pizza_object = ACTUAL_PIZZAS[pizza.lower()](size)
    pizza_object.cook()

    Delivery(delivery, pizza_object).get_pizza()


@cli.command()
def menu():
    for name, pizza in ACTUAL_PIZZAS.items():
        pizza_item = pizza()
        click.echo(
            f'- {pizza_item.name} {pizza_item.emoji}: ' +
            ', '.join(pizza_item.receipt)
        )


if __name__ == '__main__':
    cli()

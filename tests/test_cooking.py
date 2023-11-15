import unittest
from modules.cooking import Pizza, Margherita, Pepperoni, Hawaiian, get_pizzas


class TestPizza(unittest.TestCase):
    def test_pizza_instance(self):
        self.assertEqual(
            str(Pizza()), 'Pizza'
        )

    def test_pizza_equals(self):
        with self.assertRaises(ValueError):
            Pizza('XL') == Pizza('XL')

    def test_pizza_wrong_size_value(self):
        with self.assertRaises(ValueError):
            Pizza(123)

    def test_pizza_wrong_size_str(self):
        with self.assertRaises(TypeError):
            Pizza('XXXL')

    def test_pizza_dict(self):
        self.assertEqual(
            Pizza().dict(), {'Pizza': None}
        )

    def test_margherita_instance(self):
        self.assertEqual(
            str(Margherita('XL')), 'Margherita'
        )

    def test_marghertita_equals_true(self):
        self.assertEqual(
            Margherita('XL') == Margherita('XL'), True
        )

    def test_marghertita_equals_false(self):
        self.assertEqual(
            Margherita('XL') == Pepperoni('XL'), False
        )

    def test_margherita_dict(self):
        self.assertEqual(
            Margherita().dict(),
            {'Margherita': ['tomato sauce', 'mozzarella', 'tomatoes']}
        )

    def test_margherita_wrong_size(self):
        with self.assertRaises(TypeError):
            Margherita('XXXXL')

    def test_pepperoni_instance(self):
        self.assertEqual(
            str(Pepperoni('XL')), 'Pepperoni'
        )

    def test_pepperoni_equals_true(self):
        self.assertEqual(
            Pepperoni('XL') == Pepperoni('XL'), True
        )

    def test_pepperoni_equals_false(self):
        self.assertEqual(
            Pepperoni('XL') == Margherita('XL'), False
        )

    def test_pepperoni_dict(self):
        self.assertEqual(
            Pepperoni().dict(),
            {'Pepperoni': ['tomato sauce', 'mozzarella', 'pepperoni']}
        )

    def test_pepperoni_wrong_size(self):
        with self.assertRaises(TypeError):
            Pepperoni('2XL')

    def test_hawaiian_instance(self):
        self.assertEqual(
            str(Hawaiian('XL')), 'Hawaiian'
        )

    def test_hawaiian_equals_true(self):
        self.assertEqual(
            Hawaiian('XL') == Hawaiian('XL'), True
        )

    def test_hawaiian_equals_false(self):
        self.assertEqual(
            Hawaiian('XL') == Margherita('XL'), False
        )

    def test_hawaiian_dict(self):
        self.assertEqual(
            Hawaiian().dict(),
            {'Hawaiian': ['tomato sauce', 'mozzarella',
                          'chicken', 'pineapples']}
        )

    def test_hawaiian_wrong_size(self):
        with self.assertRaises(TypeError):
            Hawaiian('M')

    def test_get_pizzas_contains_pizza_classes(self):
        pizzas = get_pizzas()

        for pizza_name, pizza_class in pizzas.items():
            self.assertTrue(
                issubclass(pizza_class, Pizza),
                f'{pizza_name} class is not a subclass of Pizza'
            )


if __name__ == '__main__':
    unittest.main()

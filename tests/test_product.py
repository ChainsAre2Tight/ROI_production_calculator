import unittest
from info import cheese, pizza
from main import get_requirements_of_a_product, dict_keys_to_string


class TestProduct(unittest.TestCase):
    def test_cheese_requirements_x1(self):
        self.assertEqual(
            {
                'Cheese': 1,
                'Milk': 1.5,
                'Water': 3.25,
                'Wheat': 1.5
            },
            dict_keys_to_string(get_requirements_of_a_product(cheese, 1))
        )

    def test_cheese_requirements_x2(self):
        self.assertEqual(
            {
                'Cheese': 2,
                'Milk': 3,
                'Water': 2 + 3 + 1.5,
                'Wheat': 3
            },
            dict_keys_to_string(get_requirements_of_a_product(cheese, 2))
        )

    def test_pizza_requirements_x1(self):
        self.assertEqual(
            {
                'Cheese': 0.5,
                'Dough': 0.5,
                'Flour': 0.25,
                'Milk': 0.75,
                'Pizza': 1,
                'Vegetables': 0.5,
                'Water': 2.25,
                'Wheat': 1.0
            },
            dict_keys_to_string(get_requirements_of_a_product(pizza, 1))
        )

    def test_pizza_requirements_x4(self):
        self.assertEqual(
            {
                'Cheese': 2,
                'Dough': 2,
                'Flour': 1,
                'Milk': 3,
                'Pizza': 4,
                'Vegetables': 2,
                'Water': 9,
                'Wheat': 4,
            },
            dict_keys_to_string(get_requirements_of_a_product(pizza, 4))
        )


if __name__ == '__main__':
    unittest.main()

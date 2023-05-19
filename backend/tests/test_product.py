import unittest
from backend.information.products import cheese, pizza
from backend.functions import get_requirements_of_a_product, dict_keys_to_string, factories_from_demand, factories_to_str


class TestProduct(unittest.TestCase):
    def test_cheese_requirements_x1(self):
        self.assertEqual(
            {
                'Milk': 1.5,
                'Water': 3.25,
                'Wheat': 1.5
            },
            dict_keys_to_string(get_requirements_of_a_product(cheese, 1))
        )

    def test_cheese_requirements_x2(self):
        self.assertEqual(
            {
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
                'Vegetables': 2,
                'Water': 9,
                'Wheat': 4,
            },
            dict_keys_to_string(get_requirements_of_a_product(pizza, 4))
        )

class TestRequiredFactories(unittest.TestCase):
    def test_cheese_x8_per_15(self):
        self.assertEqual(
            {},
            factories_to_str(
                factories_from_demand(cheese, 8, 15)
            )
        )


if __name__ == '__main__':
    unittest.main()

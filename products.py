from product import Product
import factories

water = Product('Water', 15, 1, factories.water_pump, {})
wheat = Product('Wheat', 30, 2, factories.crop_farm, {water: 1})
milk = Product('Milk', 30, 1, factories.livestock_farm, {water: 1, wheat: 1})
cheese = Product('Cheese', 30, 2, factories.food_factory, {milk: 3, water: 2})

vegetables = Product('Vegetables', 30, 2, factories.crop_farm, {water: 1})
flour = Product('Flour', 30, 2, factories.food_factory, {wheat: 2})
dough = Product('Dough', 30, 2, factories.food_factory, {flour: 1, water: 1})
pizza = Product('Pizza', 30, 2, factories.food_factory, {cheese: 1, dough: 1, vegetables: 1})


from product import Product


water = Product('Water', 15, 1, {})
wheat = Product('Wheat', 30, 2, {water: 1})
milk = Product('Milk', 30, 1, {water: 1, wheat: 1})
cheese = Product('Cheese', 30, 2, {milk: 3, water: 2})

vegetables = Product('Vegetables', 30, 2, {water: 1})
flour = Product('Flour', 30, 2, {wheat: 2})
dough = Product('Dough', 30, 2, {flour: 1, water: 1})
pizza = Product('Pizza', 30, 2, {cheese: 1, dough: 1, vegetables: 1})


from backend.product import Product
from backend.information import factories

# Rise Of Industry
water = Product('Water', 15, 1, factories.water_pump, {})
wheat = Product('Wheat', 30, 2, factories.crop_farm, {water: 1})
milk = Product('Milk', 30, 1, factories.livestock_farm, {water: 1, wheat: 1})
cheese = Product('Cheese', 30, 2, factories.food_factory, {milk: 3, water: 2})

vegetables = Product('Vegetables', 30, 2, factories.crop_farm, {water: 1})
flour = Product('Flour', 30, 2, factories.food_factory, {wheat: 2})
dough = Product('Dough', 30, 2, factories.food_factory, {flour: 1, water: 1})
pizza = Product('Pizza', 30, 2, factories.food_factory, {cheese: 1, dough: 1, vegetables: 1})

leather = Product('Leather', 30, 1, factories.livestock_farm, {water: 1, wheat: 1})

# satisfactory
iron_ore = Product('Iron ore', 1 / 60, 1, factories.drill, {})

steel_ingot = Product("Steel ingot", 1 / 30, 1, factories.smeltery, {iron_ore: 1})

steel_plate = Product('Steel plate', 1 / 10, 2, factories.constructor, {steel_ingot: 3})
steel_rod = Product('Steel rod', 1 / 15, 1, factories.constructor, {steel_ingot: 1})
screws = Product('Screws', 1 / 10, 4, factories.constructor, {steel_rod: 1})

reinforced_steel_plate = Product('Reinforced_steel_plate', 1 / 5, 1, factories.assembler, {steel_plate: 6, screws: 12})
reinforced_steel_plate_alt = Product("Reinforced steel plate alternative", 1 / 5, 3, factories.assembler,
                                     {steel_plate: 18, screws: 50})
rotor = Product('Rotor', 1 / 4, 1, factories.assembler, {steel_rod: 5, screws: 25})

smart_cover = Product('Smart cover', 1/2, 1, factories.assembler, {reinforced_steel_plate: 1, rotor: 1})

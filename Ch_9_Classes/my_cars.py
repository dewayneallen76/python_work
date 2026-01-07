# Importing Multiple Classes from a Module
# You can also import multiple classes from a module. For example, if you have a module named new_car.py
# that contains both the Car and ElectricCar classes, you can import both classes like this:
from new_car import Car, ElectricCar
# You import multiple classes by separating their names with commas in the import statement.

# Now you can create instances of both classes and use their methods.
my_gas_car = Car('ford', 'mustang', 2021)
print(my_gas_car.get_descriptive_name())
my_electric_car = ElectricCar('tesla', 'model 3', 2022)
print(my_electric_car.get_descriptive_name())
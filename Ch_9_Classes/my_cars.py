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

# Importing All Classes from a Module
# If you want to import all classes from a module, you can use the asterisk (*) wildcard character.
from new_car import *
# This imports all classes defined in the new_car module. Now you can create instances of any class defined in that module.
another_gas_car = Car('honda', 'civic', 2020)
print(another_gas_car.get_descriptive_name())
another_electric_car = ElectricCar('chevrolet', 'bolt', 2021)
print(another_electric_car.get_descriptive_name())
# However, using the asterisk (*) to import everything is generally discouraged, as it can lead to confusion and make your code less readable.
# It's usually better to import only the specific classes you need.
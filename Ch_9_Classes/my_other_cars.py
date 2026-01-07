# Importing an Entire Module
# You can also import an entire module and then access the classes and functions defined in that module
# using dot notation. For example, if you have a module named new_car.py that contains both the Car and ElectricCar classes,
# you can import the entire module like this:
import new_car
# Now you can create instances of both classes using the module name.
my_gas_car = new_car.Car('chevrolet', 'camaro', 2020)
print(my_gas_car.get_descriptive_name())
my_electric_car = new_car.ElectricCar('nissan', 'leaf', 2021)
print(my_electric_car.get_descriptive_name())
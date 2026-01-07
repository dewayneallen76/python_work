from new_car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2022)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Using Aliases for Modules
# If the module name is long or might conflict with another module name, you can use an alias when importing it.
# For example, you can import the new_car module with an alias like this:
# import new_car as nc
# Then you can create instances of the classes using the alias:
# my_tesla = nc.ElectricCar('tesla', 'model s', 2022)
# This approach helps keep your code concise and avoids naming conflicts.
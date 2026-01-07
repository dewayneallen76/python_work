from new_car import Car
# Now we can make a separte file to use the Car class defined in new_car.py.
my_new_car = Car('subaru', 'outback', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(500)
my_new_car.read_odometer()

# Importing classes is an effective way to program. It allows you to keep your code organized and modular,
# making it easier to maintain and reuse. As your projects grow in complexity, using modules and imports will become increasingly important.
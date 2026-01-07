from new_car import Car
# Now we can make a separte file to use the Car class defined in new_car.py.
my_new_car = Car('subaru', 'outback', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(500)
my_new_car.read_odometer()

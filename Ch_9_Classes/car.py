# Working with Classes and Instances in Python
# Once you write a class, you'll spend most of your time working with instances created from that class.
# You can modify the attributes of an instance directly or through methods defined in the class.
class Car:
    """A simple model of a car."""

    def __init__(self, make, model, year):
        """Initialize the car's make, model, and year."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default value for odometer reading
# Setting a default value for an attribute can be done in the __init__() method. This is useful when you want all instances of
# a class to start with the same initial value for a particular attribute.
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
# Modifying Attribute Values Through Methods
# You can define methods that update an attribute's value in specific ways. This is a good way to control
# how an attribute's value is modified, especially if you want to prevent invalid values from being assigned.
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
# Incrementing an Attribute's Value
# Sometimes you'll want to increment an attribute's value instead of setting it to a specific value. 
# For example, you might want to add miles to an odometer reading.
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't increment the odometer with negative miles!")

my_car = Car('audi', 'a4', 2020)
print(my_car.get_descriptive_name())
# Modifying an Attribute's Value Directly
# You can modify an attribute's value directly through an instance. For example, you can change the
# odometer_reading attribute like this:
# my_car.odometer_reading = 23
my_car.read_odometer()
my_car.update_odometer(15000)
my_car.read_odometer()
my_car.increment_odometer(500)
my_car.read_odometer()
# my_car.increment_odometer(-100)  # This will trigger the validation message
# Importing Classes
# As you add more functionality to your classes, your files can get long, even when you use inheritance
# and composition to keep your classes properly. To help, Python allows you to store classes in modules
# and then import the classes you need into your main program file.
# A module is simply a file that contains code you want to use in another program.
# You can store your classes in a module and then import the classes you need into your main program file.
# We include a module-level docstring at the top of the file to describe its contents.
"""A class that can be used to represent a car."""

class Car:
    """A simple model of a car."""

    def __init__(self, make, model, year):
        """Initialize the car's make, model, and year."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default value for odometer reading

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't increment the odometer with negative miles!")
# Storing Multile Classes in a Module
# You can store multiple classes in a single module. For example, you might store both the Car class
# and an ElectricCar class in a module called car.py. This allows you to keep related classes together
# and makes it easier to manage your code.
class Battery:
    """A simple model of a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size  # Battery size in kWh

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            range = 200  # Default range for other battery sizes

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()  # Create a Battery instance as an attribute of ElectricCar
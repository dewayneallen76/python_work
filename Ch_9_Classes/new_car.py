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
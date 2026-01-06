# Inheritance
# When one class inherits from another, it takes on the attributes and methods of the parent class.
# This allows you to build on existing code without having to rewrite it. The new class is called
# the child class, and the class it inherits from is called the parent class.
# The child class can inherit all the attributes and methods of the parent class, and it can also define
# its own attributes and methods. This is useful when you want to create a specialized version of
# an existing class.

# existing class Car from car.py. We could also import the Car class if it were in a separate module:
# from car import Car
# Here, we'll define the Car class again for completeness.
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

# Instances as Attributes of Other Classes
# You can model complex objects by including instances of one class as attributes of another class.
# For example, you might create a Battery class and then include an instance of Battery as an attribute
# in the ElectricCar class. This allows you to organize your code better and create more modular classes.
# This approach is called composition, and it helps keep your classes focused on a single responsibility.
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

        print(f"This car can go approximately {range} miles on a full charge.")

# Now let's create a child class called ElectricCar that inherits from the Car class.
# The parent class must be part of the current file or imported before the child class is defined.
# The name of the parent class is included in parentheses in the definition of the child class.
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
# The __init__() method of the child class needs to call the __init__() method of the parent class.
# This is done using the super() function, which is a special function that allows you to
# call a method from the parent class. This allows the child class to inherit all the attributes
# defined in the parent class.
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()  # Create a Battery instance as an attribute
# once the child class is set up to inherit from the parent class, you can add attributes
# and methods specific to the child class. Here, we've added an attribute called battery_size.
    
# Overriding Methods from the Parent Class
# You can override methods from the parent class in the child class if you need to modify their behavior. To do this,
# simply define a method in the child class with the same name as the one in the parent class.
# For example, if electric cars don't have an odometer reading in the same way as traditional cars,
# you could override the read_odometer() method in the ElectricCar class.
    def read_odometer(self):
        """Print a statement showing the car's mileage with a note about electric cars."""
        print(f"This electric car has {self.odometer_reading} miles on it.")

my_leaf = ElectricCar('nissan', 'leaf', 2021)
print(my_leaf.get_descriptive_name())
my_leaf.read_odometer()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
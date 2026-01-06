# Object-oriented programming (OOP) is one of the most powerful programming paradigms in Python. 
# It allows you to model real-world entities using classes and objects, making your code more 
# organized, reusable, and easier to maintain. In this chapter, we'll explore the fundamentals of
# OOP in Python, including how to define classes, create objects, and implement key OOP concepts 
# such as inheritance and encapsulation.

class Dog:
    """A simple attempt to model a dog."""
# The __init__() method is a special method that Python runs automatically whenever we create
# a new instance based on the Dog class. The __init__() method has two leading and two trailing 
# underscores to indicate that it is a special method (also called a "dunder" method, short for 
# "double underscore"). The __init__() method allows us to define attributes that we want each 
# instance to have. The self parameter is a reference to the current instance of the class, and it is 
# used to access variables that belong to the class.
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
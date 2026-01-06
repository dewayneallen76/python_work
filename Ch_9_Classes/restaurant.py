# Try it yourself 9-1: Restaurant
#  Make a class called Restaurant. The __init__() method for Restaurant should store two 
# attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant()
# that prints these two pieces of information, and a method called open_restaurant()
# that prints a message indicating that the restaurant is open. 
#  Make an instance called restaurant from your class. Print the two attributes individually, and then 
# call both methods.
class Restaurant:
    """A simple model of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print the restaurant's name and cuisine type."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

my_restaurant = Restaurant("Pasta Palace", "Italian")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# Try it yourself 9-2: Three Restaurants
#  Start with your program from Exercise 9-1. Make two more instances from the Restaurant class. 
#  Call describe_restaurant() for each instance.
restaurant1 = Restaurant("Sushi Central", "Japanese")
restaurant2 = Restaurant("Taco Town", "Mexican")    
restaurant3 = Restaurant("Burger Barn", "American")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
# Try it yourself 9-3: Users
#  Make a class called User. Create two attributes called first_name and last_name, and
# then create several other attributes that are typically stored in a user profile. Make a
# method called describe_user() that prints a summary of the user's information. Make
# another method called greet_user() that prints a personalized greeting to the user.
#  Create several instances representing different users, and call both methods for each user.
class User:
    """A simple model of a user."""

    def __init__(self, first_name, last_name, age, email):
        """Initialize the user's first name, last name, age, and email."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")  

user1 = User("Alice", "Smith", 28, "alice.smith@example.com")
user1.describe_user()
user1.greet_user()
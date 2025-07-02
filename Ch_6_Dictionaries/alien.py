# A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and 
# you can use a key to access the value associated with that key. A key's value can be a number, 
# string, a list or even another dictionary. You can use any object that you can create in Python
# as a value in a dictionary 

# A dictionary is wrapped in braces ({}) with a series of key-value pairs inside the braces:
alien_0 = {"color" : "green", "points": 5}
# To get the value associated with a key, give the name of the dictionary and then place the key
# inside a set of square brackets:
print(alien_0["color"])

# You can add new key-value pairs to a dictionary at any time. To add a new key-value pair, you 
# would give the name of the dictionary followed by the new key in square brackets along with the
# new value: 
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# Starting with an empty dictionary
# To start filling an empty dictionary, define a dictionary with an empty set of braces, and then add
# each key-value pair on its own line:
alien_1 = {}

alien_1["color"] = "blue"
alien_1["points"] = 15

print(alien_1)

# Modifying values in a dictionary
# To modify a value in a dictionary, give the name of the dictionary with the key in square brackets
# and then the new value you want associated with that key: 
alien_1["color"] = "yellow"
print(f"The color of alien 1 is now {alien_1["color"]}.")

# Removing key-value pairs
# When you no longer need a piece of information that's stored in a dictionary, you can use the 
# del statement to completely remove a key-value pair. 
# All del needs is the name of the dictionary and the key that you want to remove: 
del alien_1["points"]
print(alien_1)
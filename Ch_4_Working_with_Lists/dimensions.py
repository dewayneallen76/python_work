# Tuples
# Sometimes you'll want to create a list of items that cannot change. Tuples allow you to do
# just that. Python refers to values that cannot change as immutable, and an immutable list is
# called a tuple. 

# Defining a tuple
# A tuple looks just like a list, except you use parentheses instead of square brackets. Once you 
# define a tuple, you can access individual elements by using each items index, just as you would
# a list. 
# For exmample, if we have a triangle that should always be a certain size, we can put the dimensions
# in a tuple: 
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# If you try to change one of the items in a tuple you will get a type error because we're trying 
# to alter a tuple, which can't be done to that type of object. Python tells us we can't assign a 
# new value to an item in a tuple: 
# dimensions[0] = 250
# TypeError: 'tuple' object does not support item assignment

# Looping through values in a tuple
# You can loop over all the values in a tuple using a for loop, just as you do with a list:
for dimension in dimensions:
    print(dimension)

# Although you can't modify a tuple, you can assign a new value to a variable that represents a tuple:
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
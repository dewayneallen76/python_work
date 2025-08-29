# Passing Arguments

# Positional arguments
# When you call a function, Python must match each argument in the function call with a parameter
# in the function definition. The simplest way to do this is based on the order of the arguments
# provided. Values matched up this way are called positional arguments 

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("cat", "archie")

# Multiple function calls
# You can call a function as many times as needed. Describing a second, different pet requires 
# just one more call to describe_pet()
describe_pet("hamster", "harry")

# Order matters in positional arguments
# You can get unexpected results if you mix up the order of the arguments in a function call when
# using positional arguments: 
describe_pet("miracle", "cow")
# In this function call we list the name first and the animal second. If you get funny results like
# this, check to make sure the order of the arguments in your function call matches the order of 
# the parameters in the function's definition. 

# Keyword arguments
# A keyword argument is a name-value pair that you pass to a function. You directly associate the
# name and the value within the argument, so when you pass the argument to the function, there's
# no confusion. Keyword arguments free you from having to worry about correctly ordering your 
# arguments in the function call, and they clarify the role of each value in the function call.
describe_pet(animal_type="dog", pet_name="stan")

# Default values
# You can define a default value for each parameter. If an argument for a parameter is provided in
# the function call, Python uses the argument value. If not, it uses the parameters default value.
# Example:
# def describe_pet(pet_name, animal_type="dog"):
# We changed the definition of describe_pet() to include a default value, 'dog', for animal_type. 
# Now when the function is called with no animal_type specified, Python knows to use the value 
# 'dog' for this parameter. 
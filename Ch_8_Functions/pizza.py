# Passing an Arbitrary Number of Arguments

# Somtimes you won't know ahead of time howm many arguments a function needs to accept.
# Fortunately, Python allows a function to collect an arbitrary number of argumnents from 
# calling the statement 

def make_pizza(*toppings):
    """Summarize the pizza we are about to make"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepporoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese', 'banana peppers')

# The asterisk in the parameter name *toppings tells Python to make a tuple called toppings, 
# containing all the values this function receives. 

# Mixing Positional and Arbitrary Arguments 
# 
# If you want a function to accept several different kinds of arguments, the parameter that accepts
# an arbitray number of arguments must be placed last in the function definition. Python matches
# positional and keyword arguments first and then collects any remaining arguments in the final 
# parameter. 
# For example, if the function needs to take a size for the pizza, that parameter must come before
# the parameter *toppings

def size_pizza(size, *toppings):
    """Summarize the size and toppings for a pizza"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

size_pizza(12, 'pepperoni')
size_pizza(16, 'pepperoni', 'ham', 'bacon', 'banana peppers')
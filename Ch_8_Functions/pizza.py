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
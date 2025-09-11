# Modifying a List in a Function
# When you pass a list to a function, the function can modify the list. Any changes you make to the
# list inside the function's body are permanent, allowing you to work more efficiently even when 
# you're dealing with large amounts of data. 

# Consider a company that creates 3D printed models of designs that users submit. Designs that need
# to be printed are stored in a list, and after being printed they're moved to a separate list. The
# following code does this without using functions 

# Start with some designs that need to be printed

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# Simulate printing each design, until none are left. 
# Move each design to completed_models after printing. 

# Adding functions to complete the same print_models(), show_completed_models()

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left. 
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

# Display all completed models.
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print(f"\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# This program is easier to extend and maintain than the version without functions. If we need to 
# print more designs later on, we can simply call the functions. If we realize the printing code
# needs to be modified, we can change the code once, and our changes will take place everywhere 
# the function is called. This technique is more efficient than having to update the code separately
# in several places in the program. 

# Every function should have one specific job. 

# Preventing a Function from Modifying a List
# Sometimes you'll want to prevent a function from modifying a list. By passing the function a 
# copy of the list, not the original. Any changes the function makes to the list will affect only
# the copy, leaving the original intact. 
# You can send a copy of a list to a function like this: 
# function_name(list_name[:])
# The slice notation [:] makes a copy of the list to send to the function. If we didn't want to
# empty the list of unprinted designs in printing_models.py, we could call print_models() like this:
# print_models(unprinted_designs[:], completed_models)
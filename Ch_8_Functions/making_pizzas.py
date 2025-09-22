# Storing Your Functions in Modules
# 
# One advantage of functions is the way they separate blocks of code from your main program. You 
# can go a step further by storing your functions in a separate file called a module and then 
# importing that module into your program. An import statement tells Python to make the code in a 
# module available in the currently running program file. 
# 
# Importing an Entire Module
# 
# To start importing functions we first need to create a module. A module is a file ending in .py
# that contains the code you want to import into your program. 
# Let's make a module that contains the function make_pizza(). To make this module, we'll remove
# everything from the file pizza.py except the function make_pizza(). 
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'pepperoni', 'extra cheese', 'green peppers', 'ham', 'bacon')

# When Python reads this file, the line import pizza tells Python to open the file pizza.py and 
# copy all the functions from it into the program. 
# This first approach to importing, in which you simply write import followed by the name of the 
# module, makes every function from the module available in your program. 
#
# Importing Specific Functions
# 
# You can also import a specific function from a module. Here's the general syntax for this 
# approach: 

# from module_name import function_name
# 
# You can import as many functions as you want from a module by separating each function's name 
# with a comma: 
# 
# from module_name import function_1, function_2, function_3
# 
# The making_pizzas.py example would look like this if we want to import just the function that we
# want to use: 
# 
# from pizza.py import make_pizza

# Using as to Give a Function an Alias
# 
# If the name of a function you're importing might conflict with an existing name in your program,
# or if the function name is long, you can use a short, unique alias - an alternate name similar
# to a nickname for the function. You'll give the function this special nickname when you import the
# function. 
# Here we give the function make_pizza() an alias, mp(), by importing make_pizza() as mp: 
# 
# from pizza import make_pizza as mp
# 
# mp(16, 'pepperoni')
# 
# The import statement show here renames the function in this program. Anytime we want to call 
# make_pizza() we can simply write mp() instead. 
# The general syntax for providing an alias is: 
# 
# from module_name import function_name as fn

# Using as to Give a Module an Alias
# 
# You can also provide an alias for module names. Giving a module a short alias, like p for pizza 
# allows you to call the module's functions more quickly. 
# 
# import pizza as p
# 
# Calling p.make_pizza() is more concise than calling pizza.make_pizza()
# The general syntax for this approach is: 
#
# import module_name as mn
# 
# Importing All Functions in a Module
# 
# from module_name import *
#
# You can tell Python to import every function in a module by using the asterisk(*) operator. 
# Because every function is imported, you can call each function without using the dot notation.
# However, it's best not to use this approach when you're working with larger modules that you didn't
# write: if the module has a function name that matches an existing name in your project, you can get 
# unexpected results. 

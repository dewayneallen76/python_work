# Functions are named blocks of code designed to do one specific job. When you want to perform
# a particular tas that you've defined in a function, you call the function responsible for it. 
# If you need to perform that task multiple times throughout your program, you don't need to type
# all the code for the same task again and again. 

# Defining a function
def greet_user():
    # docstring below describes what the funtion does 
    """Display a simple greeting"""
    print("Hello!")

# Passing information to a function
# By modifying the above function slightly it can greet the user by name. For the function to do 
# this, you enter username in the parentheses of the function's definition. By adding username, you
# allow the function to accept any value of username you specify. The function now expects you to
# provide a value for username each time the function is called. 
# Rewriting the above function
def greet_user_2(username):
    """Display a simple greeting passing value"""
    print(f"Hello, {username.title()}!")

greet_user()
greet_user_2("dewayne")

# 8-1 pg. 131
# Write a function called display_message() that prints one sentence telling everyone what you are
# learning about in this chapter. 

def display_message():
    """Tell everyone what is in this chapter"""
    print("This chapter is about Python functions.")

display_message()

#8-2 pg. 131
# Write a function called favorite_book() that accepts one parameter, title. The function should
# print a message, such as "One of my favorite books is Dungeon Crawler Carl". Call the function,
# making sure to include a book title as an argument in the function call. 

def favorite_book(title):
    """Accepts value title to display message of favorite book"""
    print(f"One of my favorite books is {title.title()}.")

favorite_book("salems lot")

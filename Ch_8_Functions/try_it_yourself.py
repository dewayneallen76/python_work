#Exercises

# 8-3 pg. 136 T-Shirt
# Write a function called make_shirt() that accepts a size and the text of a message that should
# be printed on the shirt. The function should print a sentence summarizing the size of the shirt
# and the message printed on it. Call the function using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.
def make_shirt(size, message):
    """Display shirt size and message on the shirt."""
    print(f"\nThe shirt size selected is {size.title()}.")
    print(f"The message on the shirt is {message}.")

make_shirt('large', 'This is my Python shirt')
make_shirt(message="My best shirt", size="small")

# 8-4 pg. 137 Large Shirts
# Modify the make_shirt() function so that shirts are large by default with a message that reads
# I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any 
# size with a different message. 
def python_shirt(size='large', message='I love Python'):
    """Default message for shirt and size for shirt"""
    print(f"\nShirt size: {size.title()}")
    print(f"The message on the shirt is {message}")

python_shirt()
python_shirt(size='medium')
python_shirt(size='XL', message='No step on snek')

# 8-5 pg. 137 Cities
# Write a function called describe_city() that accepts the name of a city and its country. The 
# function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter
# for the country a default value. Call your function for three different cities, at least one
# of which is not in the default country
def describe_city(city, country='japan'):
    """Displays a statement with city and country that it is in"""
    print(f"\n{city.title()} is in {country.title()}.")

describe_city('tokyo')
describe_city('san antonio', country='united states')
describe_city('kyoto')
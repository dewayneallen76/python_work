# Pythons range() function makes it easy to generate a series of numbers. 
for value in range(1, 6):
    print(value)
# The range() function causes Python to start counting at the first value you give it, 
# and stops when it reaches the second value you provide. 
# To print the numbers from 1 t0 5, you would use range(1, 6)

# If your output is different from what you expect when you're using range(), try adjusting
# your end value by 1. 

# You can also pass range() only one argument, and it will start the sequence of numbers at 0
for value in range(6):
    print(value)

# You can convert the results of range() directly into a list using the list() function
numbers = list(range(6))
print(numbers)
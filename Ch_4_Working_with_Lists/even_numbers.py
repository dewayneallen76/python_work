# We can also use the range() function to tell Python to skip numbers by passing a third argument
# to range()
# Python uses that value as a step size when generatng numbers 
even_numbers = list(range(2, 11, 2))
print(even_numbers)
# In this example, the range() function starts with the value 2 and then adds 2 to that value. 
# It adds 2 repeatedly until it reaches or passes the end value, 11 and produces this result:
# [2, 4, 6, 8, 10]

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

# List Comprehensions
# A list comprehension allows you to generate this same list in just one line of code. A list 
# comprehension combines the for loop and the creation of new elements into one line, and automatically
# appends each new element. 

# The followig exmample builds the same list of square numbers using list comprehension:
squares = [value**2 for value in range(1,11)]
print(squares)
# To use this syntax begin with a descriptive name for the list: squares
# Next, square brackets and define the expression for the values you want to store: value**2
# Then, write a for loop to generate the numbers you want to fee into the expression: for value in range(1,11)
# Note that no colon is used at the end of the for statement. 

# It takes practice to write your own list comprehensions, but you'll find them worthwhile once you 
# become comfortable creating ordinary lists. 

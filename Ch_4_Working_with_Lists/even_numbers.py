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
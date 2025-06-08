# Modifying elements in a list 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# To change an element, use the name of the list follwed by the index of the element that you want
# to change, and then provide the new value you want that item to have 

# motorcycles[0] = 'ducati'

# Adding elements to a list
#
# The simplest way to add a new element to a list is to append the item to the list. When you 
# append an item to a list, the new element is added to the end of the list. 
# append()
motorcycles.append('ducati')
print(motorcycles)

# The append() method makes is easy to build lists dynamically. For example, you can start with an
# empty list and then add items to the list using a series of append() calls. 
other_motorcycles = []
other_motorcycles.append('harley-davidson')
other_motorcycles.append('indian')
other_motorcycles.append('triumph')
print(other_motorcycles)

# Inserting elements into a list
#
# You can add a new element at any position in your list by using the insert() method. You can do 
# this by specifying the index of the new element and the value of the new item: 
other_motorcycles.insert(0, 'vanderhall')
print(other_motorcycles)

# Removing an item using the del statement
#
# If you know the position of the item you want to remove from a list, you can use the del statement
del other_motorcycles[0]
print(other_motorcycles)

# Removing an item using the pop() method
#
# The pop() method removes the last item in a list, but it lets you work with that item after 
# removing it. 
print(motorcycles)
popped_motorcyle = motorcycles.pop()
print(popped_motorcyle)

# You can use pop() to remove an item from any position in a list by including the index of the item
# in parentheses: 
last_owned_motorcycle = motorcycles.pop(2)
print(f"The last motorcyle that I owned was a {last_owned_motorcycle.title()}.")

# Removing an item by value
# 
# If you only know the value of the item you want to remove, you can use the remove() method
print(other_motorcycles)

other_motorcycles.remove('indian')
print(other_motorcycles)

# You can also use the remove() method to work with a value that's being removed from a list:
print(other_motorcycles)

too_expensive = 'harley-davidson'
other_motorcycles.remove(too_expensive)
print(other_motorcycles)
print(f"A {too_expensive.title()} costs too much for me.")
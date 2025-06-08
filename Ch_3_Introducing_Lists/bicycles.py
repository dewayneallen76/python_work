# Lists
# A list is a collection of items in a particular order
# You can put anything you want to into a list, and the items in your list don't have to be 
# related in any particular way. 
#
# Because a list usually contains more than one element, it's a good idea to make the name of your
# list plural (ex: letters, numbers, names, etc.)
#
# In Python, square brackets [] indicate a list. The elements of the list are spearated by a comma ,
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# Lists are ordered collections so you can access any element in a list by telling Python the position,
# or index of the item desired. 
#
# To access an element in a list, write the name of the list followed by the index of the item in
# square brackets:
print(bicycles[0].title())
print(bicycles[3])

# Python has a special syntax for accessing the last element in a list. If you aske for the item
# at index [-1], Python always returns the last item in the list: 
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
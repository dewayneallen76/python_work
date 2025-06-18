# You can work with a specific group of items in a list by slicing
players = ["Charles", "Martina", "Michael", "Florence", "Eli"]
print(players[0:3])

# You can generate any subset of a list. For example, if you want the second,
# third, and fourth items, you would start the slice at index 1 and end it at 4
print(players[1:4])

# If you omit the first index, Python automatically starts your slice at the 
# beginning of the list:
print(players[:4])

# If you want all items from the third item through the last item, you can start with 
# index 2, and omit the second index:
print(players[2:])

# Recall that a negative index returns and element a certain distance from the end of 
# a list. You can output any slice from the end of the list using a negative index
print(players[-3:])

# Looping through a slice
# you can use a slice in a for loop if you can to loop through a subset of the elements in
# a list. In this example we loop through the first three players and print their names:
for player in players[:3]:
    print(player.title())
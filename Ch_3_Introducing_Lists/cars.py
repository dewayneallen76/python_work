# Organizing a list
# 
# Sorting a list permanently with the sort() method
#
# Pythons sort() method makes it relatively easy to sort a list. The sort() method changes the order
# of the list permanently in alphabetical order 
cars = ['bmw', 'audi', 'toyota', 'subaru']
#cars.sort()
print(cars)

# You can also sort this list in revervse-alphabetical order by passing the argument reverse=True
# to the sort() method:
other_cars = ['ford', 'chevrolet', 'maserati', 'volkswagen', 'lexus']
other_cars.sort(reverse=True)
print(other_cars)

# Sorting a list temporarily with the sorted() function
#
# To maintain the original order of a list but present it in a sorted order, you can use the
# sorted() function. The sorted() function lets you display your list in a particular order, but
# doesn't affect the actual order of the list 

print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# Printing a list in reverse order
# 
# To reverse the original order of a list, you can use the reverse() method: 
cars.reverse()
print(cars)

# Finding the length of a list
# 
# You can quickly find the length of a list by using the len() function: 
print(len(cars))
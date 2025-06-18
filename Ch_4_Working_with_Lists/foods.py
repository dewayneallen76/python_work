# Copying a list
# To copy a list, you can make a slice that includes the entire original list by omitting the first
# and second index ([:])
my_foods = ["pizza", "sandwiches", "hot dogs", "hamburgers"]
friend_foods = my_foods[:]

my_foods.append("steak")
friend_foods.append("rice")

print("My favorite foods are:")
print(my_foods)

print("My friends favorite foods are:")
print(friend_foods)
# Often you'll need to test more than two possible situations. 
# if-elif-else
# Python runs each conditional test in order, until one passes. When a test passes, the code 
# following that test is executed and Python skips the rest of the tests. 
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# The following code produces the same result

age = 15
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")
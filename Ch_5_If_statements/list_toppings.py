requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

# Using multiple lists
available_toppings = ["mushrooms", "olives", "green peppers", "pepporoni", "pineapple", "extra cheese"]

ordered_toppings = ["mushrooms", "french fries", "extra cheese"]

for ordered_topping in ordered_toppings:
    if ordered_topping in available_toppings:
        print(f"Adding {ordered_topping}.")
    else:
        print(f"Sorry we don't have {ordered_topping}.")

print("\nFinished making your pizza!")
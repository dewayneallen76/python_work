# Rather than putting a dictionary inside a list, it's sometimes useful to put a list inside a 
# dictionary. 
# Store information about a pizza being ordered 
pizza = {
    'crust': 'thick', 
    'toppings': ['mushrooms', 'extra cheese'],
    }
# Summarize the order 
print(f"You orderd a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
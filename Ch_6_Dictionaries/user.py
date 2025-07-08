# Looping through all key-value pairs
# To see everything in a dictionary you can use a for loop. To write a for loop for a dictionary, 
# you create names for the two variables that will hold the key and value in each key-value pair:
user_0 = {
    "username": "lallen", 
    "first_name": "larry",
    "last_name": "allen",
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
# These abbreviated variables will also work: 
# for k, v in user_0.items():



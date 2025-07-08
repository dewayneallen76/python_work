# You can also use a dictionary to store one kind of information about many objects. For example,
# if you wanted to poll a group of people and ask them what their favorite programming language is.
# A dictionary is useful for storing the results of a simple poll, like this: 
favorite_language = {
    "jen": "python", 
    "sarah": "c", 
    "edward": "rust", 
    "phil": "python",
}

language = favorite_language["sarah"].title()
print(f"Sarah's favorite programming language is {language}")
# Looping through a dictionary using items() method:
for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite programming language is {language.title()}")

# Looping through all the keys in a dictionary
# The keys() method is useful when you don't need to work with all of the values in a dictionary.
friends = ["phil", "sarah"]
for name in favorite_language.keys():
    print(f"Hi {name.title()}.")
# You can access the value associated with any key you care about inside the loop, by using the 
# current key. 
    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}")

if "erin" not in favorite_language.keys():
    print("Erin, please take our poll!")

# Looping through keys is actually the default behavior when looping through a dictionary, so this
# code would have exactly the same output as above: 
for name in favorite_language:
    print(name.title())



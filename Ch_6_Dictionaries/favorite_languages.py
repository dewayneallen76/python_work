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
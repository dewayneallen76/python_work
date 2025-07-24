# When you use the input() function, Python interprets everything the user enters as a string. 
# Use the int() function to convert the input string to a numerical value. 

age = input("How old are you? ")

age = int(age)
if age >= 18:
    print(f"You are {age}. You can ride the rollercoaster!")
else:
    print(f"You are {age}. Sorry, you cannot ride the rollercoaster.")
#Using variables in strings 
first_name= "ada"
last_name= "lovelace"

#To insert a variable's value into a string, place the letter f immediately before the opening quotation mark. Put braces around the name
#or names of any variables you want to use inside the string. 
#These are called f-strings. The f is for format, because Python formats the string by replacing the name of any variable in braces with
#its value. 
full_name= f"{first_name} {last_name}"
print(full_name)
print(full_name.title())

#You can use f-strings to compose complete messages using the information associated with a variable:
print(f"Hello, {full_name.title()}!")

#You can also use f-strings to compose a message, and then assign the entire message to a variable:
message = f"Hello, {full_name.title()}!"
print(message)


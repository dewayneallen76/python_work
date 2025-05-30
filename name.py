#Changing case in a string with methods 
name = 'ada lovelace'
#The method title() appears after the variable in the print() call. A method is an action that Python can perform on a piece of data.
#The dot after name tells Python to make the title method act on the variable name. Every method is followed by a set of parentheses,
#because methods often need additional information to do their work.
#  
#The title() method changes each word to title case, where each word begins with a capital letter. 
print(name.title())

#Displays in all uppercase
print(name.upper())

#Displays in all lowercase 
print(name.lower())
#The lower() method is particularly useful for storing data. You typically won't want to trust the capitalization that your users provide,
#so you'll convert strings to lowercase before storing them. Then when you want to display the information, you'll use the case that makes
#the most sense for each string. 
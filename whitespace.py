print("Python")

#Use \t to add a tab to your text:
print("\tPython") 

#Use \n to add a newline to your text:
print("Languages:\nPython\nC\nJavaScript")

#Combine tabs and newlines in a single string:
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Stripping whitespace
#Extra whitespace can be confusing in your programs. To programmers, 'python' and ' python ' look
#pretty much the same. But to a program, they are two different strings. Python detects extra 
#space in ' python ' and considers it significant unless you tell it otherwise. 

#Python can look for extra whitespace on the right and left sides of a string. 

#To ensure that no whitespace exists at the right side of a string, use the rstrip() method:
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())

#To remove the whitespace from the string permanently, you have to associate the stripped value
#with the variable name:
favorite_language = favorite_language.rstrip()
print(favorite_language)

#To ensure that no whitespace exists at the left side of a string, use the lstrip() method:
favorite_language = ' python'
print(favorite_language)
print(favorite_language.lstrip())

favorite_language = favorite_language.lstrip()
print(favorite_language)

#You can also stripe whitespace from both sides at once using strip():
favorite_language = ' python '
print(favorite_language)
print(favorite_language.strip())

#In the real world, these stripping functions are used to most often clear up user input before
#it's stored in a program. 
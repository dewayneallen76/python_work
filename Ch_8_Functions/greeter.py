# Using a Function with a while Loop
#
# You can use functions with all the Python structures you've learned about so far. For example, 
# using the get_formatted_name() function from previous lesson formatted_name.py we can add a while
# loop to greet users more formally 
from Ch_8_Functions.formatted_name import get_formatted_name

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First Name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")




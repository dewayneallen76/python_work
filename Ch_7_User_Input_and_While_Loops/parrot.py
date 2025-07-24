# The input() function pauses your program and waits for the user to enter some text. 
# It takes one argument: the prompt that we want to display to the user, so they know what 
# kind of information to enter 
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Sometimes you'll want to write a prompt that's longer than one line. You can assign your 
# prompt to a variable and pass that variable to the input() function. This allows you to build
# your prompt over several lines, then write a clean input() statement:
prompt = "If you share your name, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# Using a while loop to to keep a program running as long as the user wants to 
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

# For a program that should run only as long as many conditions are true, you can define
# one variable that determines whether or not the entire program is active. This variable, 
# called a flag, acts as a signal to the program. We can write our programs so they run while
# the flag is to True and stop running when any of several conditions sets the value of the 
# flag to False 
# Rewriting the prompt above to use a flag instead: 
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

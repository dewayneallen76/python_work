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
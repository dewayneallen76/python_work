# Try it yourself (Lists with functions)

# 8-9. Messages
# Make a list containing a series of short text messages. Pass the list to a function called 
# show_messages(), which prints each text message. 

text_messages = ['see ya later', 'meet me at 8', 'what you doin?']

def show_messages(text_messages):
    """Displays each text message"""
    for message in text_messages:
        print(message)

show_messages(text_messages)

# 8-10. Sending Messages
# Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that
# prints each text message and moves each message to a new list called sent_messages as it's 
# printed. After calling the function, print both of your lists to make sure that the messages
# were moved correctly. 

sent_messages = []

def send_messages(text_messages, sent_messages):
   for message in text_messages:
    print(message)
    sent_messages.append(message)

send_messages(text_messages, sent_messages)
print(text_messages)
print(sent_messages)


# 8-11. Archived Messages
# Start with your work from Excercise 8-10. Call the function send_messages() with a copy of the
# list of messages. After calling the function, print both of your lists to show that the original
# list has retained its messages. 

send_messages(text_messages[:], sent_messages)
print(text_messages)
print(sent_messages)
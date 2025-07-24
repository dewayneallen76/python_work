# To exit a while loop immediately without running any remaining code in the loop, regardless
# of the results of any conditional test, use the break statement. The break statement directs
# the flow of your program; you can use it to control which lines of code are executed and which
# aren't, so the program only executes the code that you want it to, when you want it to. 
prompt = "\nPlease enter the name of a city you have visited. "
prompt += "\nEnter 'quit' when you are finished. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
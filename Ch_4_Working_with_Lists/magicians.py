magicians = ["alice", "david", "carolina"]
for magician in magicians:
    # Common practice when working with for loops, use a singular temporary variable for the list
    # magician for magicians[]
    # will print each value in the list
    print(magician) 
    # prints the value using a fstring 
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}!\n")
    
    # You can also write as many lines of code as you like in the for loop. Every indented line 
    # following the for loop is considered "inside the loop", and each indented line is executed
    # once for each value in the list. 

# Doing something after a for loop. 
# Any lines of code after the for loop that are not indented are executed once without repetition
print("Thank you everyone. That was a great magic show!")
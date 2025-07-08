# Using keys in square brackets to retrieve the value you're interested in from a dictionary might
# cause a potential problem if the key you ask for doesn't exist, you'll get an error 
# 
# In this example, when asking for the point value of an alien that doens't have a point value. 
alien_0 = {"color": "green", "speed": "slow"}
# This will result in a KeyError:
#print(alien_0["points"])

# For dictionaries specifically, you can use the get() method to set a default value that will be
# returned if the requested key doesn't exist. 
# The get() method requires a key as a first argument. As a second optional argument, you can pass
# the value to be returned if the key doens't exist:
print(alien_0.get("points", "No point value assigned."))
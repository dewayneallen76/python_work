# Using Arbitrary Keyword Arguments
#
# Sometimes you'll want to accept an arbitrary number of arguments, buy you won't know ahead of
# time what kind of information will be passed to the function. In this case, you can write functions
# that accept as many key-value pairs at the calling statement provides. 
# 
# The double asterisks before the parameter **user_info cause Python to create a dictionary called
# user_info containing all the extra name-value pairs the function receives. Within the function, 
# you can access the key-value pairs in user_info just as you would for any dictionary. 
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)
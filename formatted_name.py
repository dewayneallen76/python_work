# A function doesn't always have to display its output directly. Instead, it can process some data
# and then return a value or set of values. The value the function returns is called a return 
# value. The return statement takes a value from inside a function and sends it back to the line
# that called the function. 
# 
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# Make an Argument Optional
#
# Sometimes it makes sense to make an argument optional, so that people using the function can choose
# to provide extra information only if they want to. You can use the default values to make an
# argument optional. 

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# To make the middle name optional, we can give the middle_name argument an empty default value and
# ignore the argument unless the user provides a value. 
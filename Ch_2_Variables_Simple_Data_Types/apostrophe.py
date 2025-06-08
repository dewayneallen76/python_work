# A syntax error occurs when Python doesn't recognize a section of your program as valid Python code.
# For example, if you use an apostrophe within single quotes, you'll produce an error. 
# This happens because Python interprets everything between the first single quote and the apostrophe
# as a string. It then tries to interpret the rest of the text as Python code, which causes errors.

# In this example the apostrophe appears between double quotes, to the Python interpreter has no
# trouble reading the string correctly:
message = "One of Python's strengths is its diverse community."
print(message)

# However, if you use single quotes, Python can't identify where the string should end:
# message = 'One of Python's strengths is its diverse community.'
# print(message)

# It will produce a syntax error in the output:
# File "/Users/larryallen/Desktop/python_work/apostrophe.py", line 12
#     message = 'One of Python's strengths is its diverse community.'
#                                                                   ^
# SyntaxError: unterminated string literal (detected at line 12)
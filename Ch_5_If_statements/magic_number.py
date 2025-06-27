# Testing numerical values is pretty straightforward. For example this checks if a person is 18
age = 18
age == 18
# You can also test to see if two numbers are not equal: 
answer = 42
if answer != 42:
    print("That is not the correct answer. Please try again.")

# You can include various mathematical comparisons in your conditional statements as well, such
# as less than <, less than or equal to <=, greater than >, and greater than or equal to >=

# Using and to check multiple conditions
# Use the keyword and to combine two conditional tests
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21 
False
# if either test fails or if both fail the expression evaluates to False
age_1 = 22
age_0 >= 21 and age_1 >= 21 
True
# if each test passes, the overall expression evaluates to True

# Using or to check multiple conditions
# The keyword or allows you to check multiple conditions as well, but it passes when either or 
# both of the individual tests pass. An or expression fails only when both individual tests fail
age_0 >= 21 or age_1 >= 21
True

age_0 = 18
age_0 >= 21 or age_1 >= 21 
False
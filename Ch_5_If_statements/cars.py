# if tests let you respond to special situations correctly
# in this example, we want BMW to be printed in uppercase
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# when you want to check for equality in Python you use ==
# a single = is really a statment:
car = "audi"
# when you use == its asking a question
# Is the value of car "audi":
car == "audi"

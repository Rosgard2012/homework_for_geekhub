"""Create a Python script that takes an age as input. If the age is less than 18 or greater than 120,
 raise a custom exception called InvalidAgeError. Handle the InvalidAgeError by displaying an appropriate error message."""

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__()

try:
    age = int(input("Enter your age:  "))
    if age < 18 or age > 120:
        raise InvalidAgeError(age)
    else:
        print("You are alive, you are:  ", age)


except InvalidAgeError as e:
    print("Error: You have entered an invalid age:", e.age)
except ValueError:
    print("Error: Incorrect age format entered.")
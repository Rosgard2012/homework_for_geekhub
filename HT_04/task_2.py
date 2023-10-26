"""Create a custom exception class called NegativeValueError.
Write a Python program that takes an integer as input and raises the NegativeValueError if the input is negative.
Handle this custom exception with a try/except block and display an error message."""

class NegativeValueError(Exception):
    pass

try:
    num = int(input("Enter number: "))
    if num < 0:
        raise NegativeValueError(num)
    else:
        print("You entered positive number:", num)
except NegativeValueError as e:
    print("Error 320115: You entered negative value:", e.value)
except ValueError:
    print("Error 331111: Invalid input. Please enter a valid integer. Try again")
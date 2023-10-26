'''Write a Python program that demonstrates exception chaining. Create a custom exception class called
CustomError and another called SpecificError. In your program (could contain any logic you want), raise a SpecificError,
 and then catch it in a try/except block, re-raise it as a CustomError with the original exception as the cause.
  Display both the custom error message and the original exception message.'''


class CustomError(Exception):
    pass

class SpecificError(Exception):
    pass

try:

    raise SpecificError("This is a specific error.")
except SpecificError as specific_exception:
    try:

        raise CustomError("This is custom error.") from specific_exception
    except CustomError as custom_exception:

        print("Custom Error message:  ", custom_exception)
        print("Original Exception Message:  ", custom_exception.__cause__)
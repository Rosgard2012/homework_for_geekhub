"""Create a Python program that repeatedly prompts the user for a number until a valid integer is provided.
 Use a try/except block to handle any ValueError exceptions, and keep asking for input until a valid integer is entered.
  Display the final valid integer."""




while True:
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        print("You entered a valid integer: ", number)
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
#4. Write a script which accepts a <number> from user and then <number> times asks user for string input.
#   At the end script must print out result of concatenating all <number> strings.

number = int(input("Enter a <number>: "))
result = ""
for i in range(number):
    user_input = input(f"Enter string #{i + 1}: ")
    result += user_input
print("Concatenated result: ", result)
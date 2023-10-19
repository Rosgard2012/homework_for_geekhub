# 3. Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers.

number = int(input("Enter a <number>: "))

if number <= 0:
    print("write a positive number")
else:
    sum_of_integers = 0
    for i in range(1, number + 1):
        sum_of_integers += i
    print(f"The sum of the first {number} positive integers is: {sum_of_integers}")
'''3. Програма-банкомат.
   Використувуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль
      (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс
      (файл <{username}_balance.TXT>) та історію транзакцій
      (файл <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова
      перевірка введених даних (введено цифри; знімається не більше,
       ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу
      (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка
      додається в кінець файла;
      - файл з користувачами: тільки читається. Але якщо захочете
      реалізувати функціонал додавання нового користувача - не стримуйте
       себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow
       банкомата:
      - на початку роботи - логін користувача (програма запитує ім'я/пароль).
       Якщо вони неправильні - вивести повідомлення про це і закінчити роботу
        (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на
         ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал, але основне
       завдання має бути повністю реалізоване :)
    P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json
     відповідно)
    P.S.S. Добре продумайте структуру програми та функцій (edited)
'''

import csv
import json
import os


def load_user_data():
    users = []
    with open('for_task_03/users.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(row)
    return users


def login():
    attempts = 3
    while attempts > 0:
        username = input("Введіть ім'я: ")
        password = input("Введіть пароль: ")

        users = load_user_data()
        for user in users:
            if user['username'] == username and user['password'] == password:
                return user
        print("Неправильне ім'я або пароль. Спробуйте ще раз.")
        attempts -= 1

    print("Ви вичерпали всі спроби. До побачення!")
    exit()


def load_balance(username):
    filename = f"for_task_03/balance/{username}_balance.txt"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return float(file.read())
    else:
        return 0.0


def update_balance(username, new_balance):
    filename = f"for_task_03/balance/{username}_balance.txt"
    with open(filename, 'w') as file:
        file.write(str(new_balance))


def load_transactions(username):
    filename = f"for_task_03/transactions/{username}_transactions.json"
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return []


def save_transaction(username, transaction):
    filename = f"for_task_03/transactions/{username}_transactions.json"
    transactions = load_transactions(username)
    transactions.append(transaction)
    with open(filename, 'w') as file:
        json.dump(transactions, file, indent=2)


def view_balance(username):
    balance = load_balance(username)
    print(f"Поточний баланс: {balance} грн")


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Неправильний формат введених даних. Будь ласка, введіть числове значення.")


def deposit(username):
    amount = get_float_input("Введіть суму для внесення: ")
    if amount > 0:
        balance = load_balance(username)
        new_balance = balance + amount
        update_balance(username, new_balance)
        transaction = {"action": "deposit", "amount": amount}
        save_transaction(username, transaction)
        print(f"Гроші внесено успішно. Новий баланс: {new_balance} грн")
    else:
        print("Введіть додатню суму.")


def withdraw(username):
    amount = float(input("Введіть суму для зняття: ").replace(',', '.'))
    balance = load_balance(username)
    if 0 < amount <= balance:
        new_balance = balance - amount
        update_balance(username, new_balance)
        transaction = {"action": "withdraw", "amount": amount}
        save_transaction(username, transaction)
        print(f"Гроші знято успішно. Новий баланс: {new_balance} грн")
    elif amount <= 0:
        print("Введіть додатню суму.")
    else:
        print("Недостатньо коштів на рахунку.")


def start():
    user = login()

    while True:
        print("\nВведіть дію:")
        print("1. Продивитись баланс")
        print("2. Поповнити баланс")
        print("3. Зняти кошти")
        print("4. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            view_balance(user['username'])
        elif choice == '2':
            deposit(user['username'])
        elif choice == '3':
            withdraw(user['username'])
        elif choice == '4':
            print("Дякуємо за використання нашого банкомату. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    start()

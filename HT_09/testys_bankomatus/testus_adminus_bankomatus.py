
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


def is_admin(username, password):
    return username == "admin" and password == "admin"


def login():
    attempts = 3
    while attempts > 0:
        username = input("Введіть ім'я: ")
        password = input("Введіть пароль: ")

        if is_admin(username, password):
            print("Ви увійшли як адміністратор.")
            return {"username": username, "is_admin": True}

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
        with open(filename, 'w') as file:
            file.write('0.0')
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
        with open(filename, 'w') as file:
            json.dump([], file)
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


def add_user():
    new_username = input("Введіть нове ім'я користувача: ")
    new_password = input("Введіть пароль для нового користувача: ")

    users = load_user_data()
    for user in users:
        if user['username'] == new_username:
            print("Користувач з таким ім'ям вже існує.")
            return
    with open('for_task_03/users.csv', 'a', newline='') as csvfile:
        fieldnames = ['username', 'password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'username': new_username, 'password': new_password})

    print(f"Користувач {new_username} успішно доданий.")

def delete_user():
    username_to_delete = input("Введіть ім'я користувача, якого ви хочете видалити: ")

    users = load_user_data()
    filtered_users = [user for user in users if user['username'] != username_to_delete]

    # Запис нового списку користувачів у CSV-файл
    with open('for_task_03/users.csv', 'w', newline='') as csvfile:
        fieldnames = ['username', 'password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_users)

    print(f"Користувач {username_to_delete} успішно видалений.")


def view_all_balances():
    users = load_user_data()
    for user in users:
        balance = load_balance(user['username'])
        print(f"Користувач: {user['username']}, Баланс: {balance} грн")


def start():
    user = login()

    while True:
        print("\nВведіть дію:")
        print("1. Продивитись баланс")
        print("2. Поповнити баланс")
        print("3. Зняти кошти")
        print("4. Додати користувача" if user.get("is_admin")  else "5. Видалити користувача" if user.get("is_admin") else "6. Подивитися баланс всіх користувачів" if user.get("is_admin") else "7. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            view_balance(user['username'])
        elif choice == '2':
            deposit(user['username'])
        elif choice == '3':
            withdraw(user['username'])
        elif choice == '4' and user.get("is_admin"):
            add_user()
        elif choice == '5' and user.get("is_admin"):
            delete_user()
        elif choice == '6' and user.get("is_admin"):
            view_all_balances()
        elif choice == '7':
            print("Дякуємо за використання нашого банкомату. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    start()

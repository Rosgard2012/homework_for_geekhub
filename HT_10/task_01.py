import sqlite3
import re


def load_user_data(username):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user_data = cursor.fetchone()

    conn.close()
    return user_data


def login():
    attempts = 3
    while attempts > 0:
        username = input("Введіть ім'я: ")
        password = input("Введіть пароль: ")

        user = load_user_data(username)
        if user and user[2] == password:
            return user
        else:
            print("Неправильне ім'я або пароль. Спробуйте ще раз.")
            attempts -= 1

    print("Ви вичерпали всі спроби. До побачення!")
    exit()


def create_new_user():
    username = input("Введіть нове ім'я користувача: ")
    password = input("Введіть пароль: ")

    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=?', (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("Користувач з таким ім'ям вже існує. Спробуйте інше ім'я.")
        conn.close()
        return

    if (len(password) < 8 or not any(char.isdigit() for char in password)
                          or not any(char.isalpha() for char in password)
                          or not any(char.isupper() for char in password)
                          or not any(char.islower() for char in password)):
        print("Пароль повинен містити мінімум 8 символів, один знак"
              " принаймні одну цифру, одну букву верхнього та нижнього регістру.")
        conn.close()
        return

    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    print("Новий користувач успішно створений.")

    conn.close()


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Будь ласка, введіть коректне число.")


def update_balance(username, new_balance):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE users SET balance = ? WHERE username = ?', (new_balance, username))
    conn.commit()

    conn.close()


def save_transaction(username, transaction_type, amount):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
    user_id = cursor.fetchone()[0]

    cursor.execute('INSERT INTO transactions (user_id, action, amount) VALUES (?, ?, ?)',
                   (user_id, transaction_type, amount))
    conn.commit()

    conn.close()


def is_valid_amount(amount, atm_balance):
    if amount <= 0:
        print("Введіть додатню суму.")
        return False
    elif amount % 10 != 0:
        print("Неприпустима сума для зняття. Сума повинна бути кратною 10.")
        return False
    elif amount > atm_balance:
        print("Недостатньо коштів в банкоматі.")
        return False
    else:
        return True


def load_atm_balance():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM banknotes')
    notes_data = cursor.fetchone()

    conn.close()

    atm_balance = (notes_data[1] * 10) + (notes_data[2] * 20) + (notes_data[3] * 50) + \
                  (notes_data[4] * 100) + (notes_data[5] * 200) + (notes_data[6] * 500) + \
                  (notes_data[7] * 1000)

    return atm_balance


def deposit(username):
    amount = get_float_input("Введіть суму для внесення: ")
    if amount > 0:
        if is_valid_amount(amount, load_atm_balance()):
            balance = load_balance(username)
            new_balance = balance + amount
            update_balance(username, new_balance)
            save_transaction(username, 'deposit', amount)
            print(f"Гроші внесено успішно. Новий баланс: {new_balance} грн")
        else:
            rest = amount % 10
            deposit_amount = amount - rest
            balance = load_balance(username)
            new_balance = balance + deposit_amount
            update_balance(username, new_balance)
            save_transaction(username, 'deposit', deposit_amount)
            print(f"Банкомат прийняв {deposit_amount} грн. Решта {rest} грн повертається.")
    else:
        print("Введіть додатню суму.")


def withdraw(username):
    amount = get_float_input("Введіть суму для зняття: ")
    user_balance = load_balance(username)
    atm_balance = load_atm_balance()

    if is_valid_amount(amount, atm_balance):
        if amount > user_balance:
            print("Недостатньо коштів на рахунку.")
        else:
            new_balance = user_balance - amount
            update_balance(username, new_balance)
            save_transaction(username, 'withdraw', amount)
            print(f"Гроші знято успішно. Новий баланс: {new_balance} грн")
            # update_atm_balance_after_withdrawal(amount)
    else:
        print("Помилка: Неприпустима сума для зняття.")


def is_cashier(username):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('SELECT is_cashier FROM users WHERE username = ?', (username,))
    is_cashier = cursor.fetchone()[0]

    conn.close()
    return is_cashier == 1


def manage_atm(username):
    print("Ви увійшли як інкасатор.")
    while True:
        print("\nВведіть дію:")
        print("1. Змінити кількість купюр в банкоматі")
        print("2. Подивитися залишок купюр в банкоматі")
        print("3. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            change_notes(username)
        elif choice == '2':
            view_notes_ink(username)
        elif choice == '3':
            print("Дякуємо за роботу. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Будь ласка, введіть ціле число.")


def change_notes(username):
    if not is_cashier(username):
        print("У вас немає прав для цієї операції.")
        return

    print("Змінити кількість купюр в банкоматі.")
    notes_10 = get_int_input("Кількість купюр номіналом 10: ")
    notes_20 = get_int_input("Кількість купюр номіналом 20: ")
    notes_50 = get_int_input("Кількість купюр номіналом 50: ")
    notes_100 = get_int_input("Кількість купюр номіналом 100: ")
    notes_200 = get_int_input("Кількість купюр номіналом 200: ")
    notes_500 = get_int_input("Кількість купюр номіналом 500: ")
    notes_1000 = get_int_input("Кількість купюр номіналом 1000: ")

    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE banknotes SET
        notes_10 = ?,
        notes_20 = ?,
        notes_50 = ?,
        notes_100 = ?,
        notes_200 = ?,
        notes_500 = ?,
        notes_1000 = ?
    ''', (notes_10, notes_20, notes_50, notes_100, notes_200, notes_500, notes_1000))

    conn.commit()
    conn.close()

    print("Кількість купюр в банкоматі успішно оновлено.")


def view_notes_ink(username):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM banknotes')
    notes_data = cursor.fetchone()

    conn.close()

    print("\nКількість купюр в банкоматі:")
    print(f"Номінал 10: {notes_data[1]}")
    print(f"Номінал 20: {notes_data[2]}")
    print(f"Номінал 50: {notes_data[3]}")
    print(f"Номінал 100: {notes_data[4]}")
    print(f"Номінал 200: {notes_data[5]}")
    print(f"Номінал 500: {notes_data[6]}")
    print(f"Номінал 1000: {notes_data[7]}")


def view_notes(username):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('SELECT balance FROM users WHERE username = ?', (username,))
    user_balance = cursor.fetchone()[0]

    conn.close()

    print(f"\nБаланс на рахунку користувача {username}: {user_balance} грн")


def load_balance(username):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('SELECT balance FROM users WHERE username = ?', (username,))
    balance = cursor.fetchone()[0]

    conn.close()
    return balance


def start():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    while True:
        print("\nВведіть дію:")
        print("1. Увійти")
        print("2. Створити нового користувача")
        print("3. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            user = login()
            if user:
                if user[1] == 'admin' and user[2] == 'admin':
                    manage_atm(user[1])
                else:
                    perform_user_actions(user[1])
        elif choice == '2':
            create_new_user()
        elif choice == '3':
            print("Дякуємо за використання нашого банкомату. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


def perform_user_actions(username):
    while True:
        print("\nВведіть дію:")
        print("1. Продивитись баланс")
        print("2. Поповнити баланс")
        print("3. Зняти кошти")
        print("4. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            view_notes(username)
        elif choice == '2':
            deposit(username)
        elif choice == '3':
            withdraw(username)
        elif choice == '4':
            print("Дякуємо за використання нашого банкомату. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    start()
#бугага
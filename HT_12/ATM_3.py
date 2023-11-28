
import sqlite3
from pathlib import Path
import random

BASE_DIR = Path(__file__).parent
DB_PATH = Path(BASE_DIR, "bank.db")

class BankSystem:
    def __init__(self):
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()


    def load_user_data(self, username):
        self.cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user_data = self.cursor.fetchone()
        return user_data

    def login(self):
        attempts = 3
        while attempts > 0:
            username = input("Введіть ім'я: ")
            password = input("Введіть пароль: ")

            user = self.load_user_data(username)
            if user and user[2] == password:
                return user
            else:
                print("Неправильне ім'я або пароль. Спробуйте ще раз.")
                attempts -= 1

        print("Ви вичерпали всі спроби. До побачення!")
        exit()

    def create_new_user(self):
        username = input("Введіть нове ім'я користувача: ")
        password = input("Введіть пароль: ")

        self.cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        existing_user = self.cursor.fetchone()

        if existing_user:
            print("Користувач з таким ім'ям вже існує. Спробуйте інше ім'я.")
            return

        if (len(password) < 8 or not any(char.isdigit() for char in password)
                              or not any(char.isalpha() for char in password)
                              or not any(char.isupper() for char in password)
                              or not any(char.islower() for char in password)):
            print("Пароль повинен містити мінімум 8 символів, один знак"
                  " принаймні одну цифру, одну букву верхнього та нижнього регістру.")
            return

        if random.random() < 0.1:
            bonus_amount = random.uniform(50, 200)
            print(f"Вітаємо! Ви отримали бонус {bonus_amount} грн.")
        else:
            bonus_amount = 0

        self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        self.connection.commit()
        print("Новий користувач успішно створений.")



    def get_float_input(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Будь ласка, введіть коректне число.")

    def update_balance(self, username, new_balance):
        self.cursor.execute('UPDATE users SET balance = ? WHERE username = ?', (new_balance, username))
        self.connection.commit()


    def save_transaction(self, username, transaction_type, amount):
        self.cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        user_id = self.cursor.fetchone()[0]

        self.cursor.execute('INSERT INTO transactions (user_id, action, amount) VALUES (?, ?, ?)',
                                (user_id, transaction_type, amount))
        self.connection.commit()


    def is_valid_amount(self, amount, atm_balance):
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


    def load_atm_balance(self):
            self.cursor.execute('SELECT * FROM banknotes')
            notes_data = self.cursor.fetchone()

            atm_balance = (notes_data[1] * 10) + (notes_data[2] * 20) + (notes_data[3] * 50) + \
                          (notes_data[4] * 100) + (notes_data[5] * 200) + (notes_data[6] * 500) + \
                          (notes_data[7] * 1000)

            return atm_balance



    def deposit(self, username):
        amount = self.get_float_input("Введіть суму для внесення: ")
        if amount > 0:
            if self.is_valid_amount(amount, self.load_atm_balance()):
                balance = self.load_balance(username)
                new_balance = balance + amount
                self.update_balance(username, new_balance)
                self.save_transaction(username, 'deposit', amount)
                print(f"Гроші внесено успішно. Новий баланс: {new_balance} грн")
            else:
                rest = amount % 10
                deposit_amount = amount - rest
                balance = self.load_balance(username)
                new_balance = balance + deposit_amount
                self.update_balance(username, new_balance)
                self.save_transaction(username, 'deposit', deposit_amount)
                print(f"Банкомат прийняв {deposit_amount} грн. Решта {rest} грн повертається.")
        else:
            print("Введіть додатню суму.")

    def withdraw_cash(self, amount, username):
        if amount <= 0:
            print("Сума має бути додатньою.")
            return None

        self.cursor.execute('SELECT balance FROM users WHERE username = ?', (username,))
        user_balance = self.cursor.fetchone()

        if not user_balance:
            print("Користувача з таким логіном не знайдено.")
            return None

        user_balance = user_balance[0]

        if amount > user_balance:
            print("У вас недостатньо коштів на рахунку.")
            return None

        if amount % 10 != 0:
            print(f"Неможливо зняти суму {amount} грн.")
            return None

        i = 7
        available_denominations_copy = [10, 20, 50, 100, 200, 500, 1000]
        remaining_amount = amount
        to_withdraw = {}

        atm_money = self.cursor.execute(
            "SELECT notes_10, notes_20, notes_50, notes_100, notes_200, notes_500, notes_1000 FROM banknotes").fetchone()

        while i > 0 and remaining_amount > 0:
            remaining_amount = amount
            to_withdraw = {}
            atm_money = list(atm_money)
            atm_money_10 = int(atm_money[0])
            atm_money_20 = int(atm_money[1])

            if amount % 50 != 0 or atm_money_10 == 0 or atm_money_20 > 2 or amount > 40:
                atm_money[1] = atm_money[1] - 3
                atm_money.insert(3, 1)
                available_denominations_copy.insert(4, 60)

            for denom in sorted(available_denominations_copy, reverse=True):
                count = min(remaining_amount // denom, atm_money[available_denominations_copy.index(denom)])
                if count > 0:
                    to_withdraw[denom] = count
                    remaining_amount -= count * denom

            try:
                available_denominations_copy.pop(i)
            except IndexError:
                pass

            i -= 1

        if remaining_amount == 0:
            self.cursor.execute("UPDATE users SET balance = balance - ? WHERE username=?", (amount, username))
            self.connection.commit()
            print(f"Успішно знято {amount} грн\n")

            print("Купюри для видачі:")
            for denom, count in to_withdraw.items():
                equiv_denom = denom
                equiv_count = count
                if equiv_denom == 60:
                    equiv_count = 3
                    equiv_denom = 20

                print(f"{equiv_denom} грн: {equiv_count} купюрами")

            else:
                print(f"Неможливо зняти суму {amount} грн через обмеження в наявності купюр у банкоматі.\n")
                return None

    def withdraw(self, username):
        amount = self.get_float_input("Введіть суму для зняття: ")
        user_balance = self.load_balance(username)

        if not self.is_valid_amount(amount, self.load_atm_balance()):
            print("Помилка: Неприпустима сума для зняття.")
            return

        if amount > user_balance:
            print("Недостатньо коштів на рахунку")
            return

        withdrawal_info = self.withdraw_cash(amount, username)
        if withdrawal_info:
            amount_withdrawn, to_withdraw = withdrawal_info
            new_balance = user_balance - amount_withdrawn
            self.update_balance(username, new_balance)
            self.save_transaction(username, 'withdraw', amount_withdrawn)
            print(f"Гроші знято успішно. Новий баланс: {new_balance} грн")

            print("Купюри для видачі:")
            for denom, count in to_withdraw.items():
                print(f"{denom} грн: {count} купюрами")
        else:
            print(f"Неможливо зняти суму {amount} грн через обмеження в наявності купюр у банкоматі.")


    def is_cashier(self, username):
            self.cursor.execute('SELECT is_cashier FROM users WHERE username = ?', (username,))
            is_cashier = self.cursor.fetchone()[0]
            return is_cashier == 1

    def manage_atm(self, username):
        print("Ви увійшли як інкасатор.")
        while True:
            print("\nВведіть дію:")
            print("1. Змінити кількість купюр в банкоматі")
            print("2. Подивитися залишок купюр в банкоматі")
            print("3. Вихід")

            choice = input("Ваш вибір: ")

            if choice == '1':
                self.change_notes(username)
            elif choice == '2':
                self.view_notes_ink(username)
            elif choice == '3':
                print("Дякуємо за роботу. До побачення!")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

    def get_int_input(self, prompt):
            while True:
                try:
                    value = int(input(prompt))
                    return value
                except ValueError:
                    print("Будь ласка, введіть ціле число.")

    def change_notes(self, username):
            if not self.is_cashier(username):
                print("У вас немає прав для цієї операції.")
                return

            print("Змінити кількість купюр в банкоматі.")
            notes_10 = self.get_int_input("Кількість купюр номіналом 10: ")
            notes_20 = self.get_int_input("Кількість купюр номіналом 20: ")
            notes_50 = self.get_int_input("Кількість купюр номіналом 50: ")
            notes_100 = self.get_int_input("Кількість купюр номіналом 100: ")
            notes_200 = self.get_int_input("Кількість купюр номіналом 200: ")
            notes_500 = self.get_int_input("Кількість купюр номіналом 500: ")
            notes_1000 = self.get_int_input("Кількість купюр номіналом 1000: ")

            self.cursor.execute('''
                UPDATE banknotes SET
                notes_10 = ?,
                notes_20 = ?,
                notes_50 = ?,
                notes_100 = ?,
                notes_200 = ?,
                notes_500 = ?,
                notes_1000 = ?
            ''', (notes_10, notes_20, notes_50, notes_100, notes_200, notes_500, notes_1000))

            self.connection.commit()
            print("Кількість купюр в банкоматі успішно оновлено.")


    def view_notes_ink(self, username):
#        self.cursor.execute
        self.cursor.execute('SELECT * FROM banknotes  WHERE id = 1')

        notes_data = self.cursor.fetchone()

        print("\nКількість купюр в банкоматі:")
        print(f"Номінал 10: {notes_data[1]}")
        print(f"Номінал 20: {notes_data[2]}")
        print(f"Номінал 50: {notes_data[3]}")
        print(f"Номінал 100: {notes_data[4]}")
        print(f"Номінал 200: {notes_data[5]}")
        print(f"Номінал 500: {notes_data[6]}")
        print(f"Номінал 1000: {notes_data[7]}")

    def view_notes(self, username):
        self.cursor.execute('SELECT balance FROM users WHERE username = ?', (username,))
        user_balance = self.cursor.fetchone()[0]

        print(f"\nБаланс на рахунку користувача {username}: {user_balance} грн")

    def load_balance(self, username):
        self.cursor.execute('SELECT balance FROM users WHERE username = ?', (username,))
        balance = self.cursor.fetchone()[0]
        return balance

    def perform_user_actions(self, username):
        while True:
            print("\nВведіть дію:")
            print("1. Продивитись баланс")
            print("2. Поповнити баланс")
            print("3. Зняти кошти")
            print("4. Вихід")

            choice = input("Ваш вибір: ")

            if choice == '1':
                self.view_notes(username)
            elif choice == '2':
                self.deposit(username)
            elif choice == '3':
                amount = self.get_float_input("Введіть суму для зняття: ")
                self.withdraw_cash(amount, username) if amount > 0 else print("Введіть додатню суму.")
            elif choice == '4':
                print("Дякуємо за використання нашого банкомату. До побачення!")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")


    def start(self):
        while True:
            print("\nВведіть дію:")
            print("1. Увійти")
            print("2. Створити нового користувача")
            print("3. Вихід")

            choice = input("Ваш вибір: ")

            if choice == '1':
                user = self.login()
                if user:
                    if user[1] == 'admin' and user[2] == 'admin':
                        self.manage_atm(user[1])
                    else:
                        self.perform_user_actions(user[1])
            elif choice == '2':
                self.create_new_user()
            elif choice == '3':
                print("Дякуємо за використання нашого банкомату. До побачення!")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

        self.connection.close()


if __name__ == "__main__":
    bank_system = BankSystem()
    bank_system.start()
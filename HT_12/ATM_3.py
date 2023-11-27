import sqlite3
from pathlib import Path
import random


BASE_DIR = Path(__file__).parent
DB_PATH = Path(BASE_DIR, "bank.db")


class ATM:
    def __init__(self, path=DB_PATH):
        self.path = path
#        self.conn = sqlite3.connect(DB_PATH)
#        self.cursor = self.conn.cursor()


    def start(self):
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.conn.close()
        print("Дякуємо за роботу. До побачення!")





"""    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT,
                is_cashier INTEGER DEFAULT 0,
                balance REAL DEFAULT 0.0
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                action TEXT,
                amount REAL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS banknotes (
                id INTEGER PRIMARY KEY,
                notes_10 INTEGER,
                notes_20 INTEGER,
                notes_50 INTEGER,
                notes_100 INTEGER,
                notes_200 INTEGER,
                notes_500 INTEGER,
                notes_1000 INTEGER
            )
        ''')

        self.cursor.executemany('''
            INSERT INTO users (username, password, is_cashier) VALUES (?, ?, ?)
        ''', [
            ('Petro', '1234', 0),
            ('Stepan', '4321', 0),
            ('Vasyl', '1111', 0),
            ('admin', 'admin', 1)
        ])

        self.cursor.execute('''
            INSERT INTO banknotes (
                notes_10, notes_20, notes_50, notes_100, notes_200, notes_500, notes_1000
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (10, 10, 10, 10, 10, 10, 10))

        self.conn.commit()

    def get_int_input(self, message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Невірне значення. Спробуйте ще раз.")

    def get_user(self, username):
        self.cursor.execute('''
            SELECT * FROM users WHERE username = ?
        ''', (username,))

        return self.cursor.fetchone()

    def is_cashier(self, username):
        user = self.get_user(username)
        return user[3] == 1

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
                self.view_notes()
            elif choice == '3':
                print("Дякуємо за роботу. До побачення!")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")
                
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

        self.conn.commit()
        
        
    def view_notes(self):
        self.cursor.execute('''
            SELECT * FROM banknotes
        ''')

        notes = self.cursor.fetchone()
        print(f"Кількість купюр номіналом 10: {notes[1]}")
        print(f"Кількість купюр номіналом 20: {notes[2]}")
        print(f"Кількість купюр номіналом 50: {notes[3]}")
        print(f"Кількість купюр номіналом 100: {notes[4]}")
        print(f"Кількість купюр номіналом 200: {notes[5]}")
        print(f"Кількість купюр номіналом 500: {notes[6]}")
        print(f"Кількість купюр номіналом 1000: {notes[7]}")
        
    def view_balance(self, username):
        user = self.get_user(username)
        print(f"Ваш баланс: {user[4]}")
        
    def withdraw_money(self, username):
        """
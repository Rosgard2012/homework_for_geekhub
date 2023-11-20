import sqlite3


def create_tables():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            is_cashier INTEGER DEFAULT 0,
            balance REAL DEFAULT 0.0
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            action TEXT,
            amount REAL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    cursor.execute('''
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


    cursor.executemany('''
        INSERT INTO users (username, password, is_cashier) VALUES (?, ?, ?)
    ''', [
        ('Petro', '1234', 0),
        ('Stepan', '4321', 0),
        ('Vasyl', '1111', 0),
        ('admin', 'admin', 1)
    ])


    cursor.execute('''
        INSERT INTO banknotes (
            notes_10, notes_20, notes_50, notes_100, notes_200, notes_500, notes_1000
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (10, 10, 10, 10, 10, 10, 10))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()

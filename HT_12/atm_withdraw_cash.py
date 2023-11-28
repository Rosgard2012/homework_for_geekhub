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



def withdraw_cash(self, amount, username):
    if amount <= 0:
        print("Сума має бути додатньою.")
        return None

    self.cursor.execute('SELECT balance FROM users WHERE username = ?', (username,))
    user_balance = self.cursor.fetchone()

    if not user_balance:
        print("Користувача з таким логіном не знайдено.")
        return None

    user_balance = user_balance[0]  # Витягнути значення з кортежу

    if amount > user_balance:
        print("У вас недостатньо коштів на рахунку.")
        return None

    if amount % 10 != 0:
        print(f"Неможливо зняти суму {amount} грн.")
        return None

    available_denominations = [1000, 500, 200, 100, 50, 20, 10]
    to_withdraw = {}

    atm_money = self.cursor.execute(
        "SELECT notes_10, notes_20, notes_50, notes_100, notes_200, notes_500, notes_1000 FROM banknotes").fetchone()

    remaining_amount = amount
    for denom in available_denominations:
        count = min(remaining_amount // denom, atm_money[available_denominations.index(denom)])
        if count > 0:
            to_withdraw[denom] = count
            remaining_amount -= count * denom

    if remaining_amount == 0:
        self.cursor.execute("UPDATE users SET balance = balance - ? WHERE username=?", (amount, username))
        self.connection.commit()
        return amount, to_withdraw

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

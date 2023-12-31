def atm_transaction(bills_available, amount): # Перевірка на наявність купюр та суми для видачі
    # методом рекурсії
    # Логіка для зняття коштів з банкомату
    bills = [1000, 500, 200, 100, 50, 20, 10] # Доступні номінали купюр
    bill_count = {bill: count for bill, count in zip(bills, bills_available)} # Словник з кількістю купюр

    def withdraw(amount_left, start_bill): # Рекурсивний виклик функції
        if amount_left == 0:        # Базовий випадок
            return {}               # Повернути словник з кількістю купюр для видачі
        if amount_left < 0 or start_bill == len(bills): # Базовий випадок
            return None            # Повернути None, якщо видача неможлива

        current_bill = bills[start_bill] # Поточний номінал купюри
        max_count = min(amount_left // current_bill, bill_count[current_bill]) # Максимальна кількість купюр для видачі
        for count in range(max_count, -1, -1):  # Перебір кількості купюр для видачі
            result = withdraw(amount_left - count * current_bill, start_bill + 1) # Рекурсивний виклик функції
            if result is not None: # Якщо видача можлива
                if count > 0: # Якщо кількість купюр більше 0
                    result[current_bill] = count # Збереження кількості купюр для видачі
                return result # Повернути словник з кількістю купюр для видачі

        return None

    result = withdraw(amount, 0) # Рекурсивний виклик функції
    if result is not None: # Якщо видача можлива
        return result # Повернути словник з кількістю купюр для видачі
    else:
        return "Неможливо видача даної суми"

# Приклади використання для перевірки
bills_available_1 = [1, 1, 4, 0, 1, 6, 0]
amount_1 = 110
print(atm_transaction(bills_available_1, amount_1))  # Очікуваний результат: {50: 1, 20: 3}

bills_available_2 = [5, 1, 4, 0, 1, 1, 5]
amount_2 = 1170
print(atm_transaction(bills_available_2, amount_2))  # Очікуваний результат: {500: 1, 200: 3, 50: 1, 20: 1}

bills_available_3 = [10, 10, 10, 10, 10, 10, 0]
amount_3 = 160
print(atm_transaction(bills_available_3, amount_3))  # Очікуваний результат: {100: 1, 20: 3}

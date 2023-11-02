"""2. Написати функцію <bank> , яка працює за наступною логікою:
 користувач робить вклад у розмірі <a> одиниць строком на <years> років
 під <percents> відсотків (кожен рік сума вкладу збільшується на цей
 відсоток, ці гроші додаються до суми вкладу і в наступному році на
 них також нараховуються відсотки). Параметр <percents> є необов'язковим
 і має значення по замовчуванню <10> (10%). Функція повинна
 принтануть суму, яка буде на рахунку, а також її повернути
 (але округлену до копійок)."""


def bank(a, years, percents=10):
    total_sum = a
    for year in range(years):
        total_sum += total_sum * (percents / 100)
    total_amount = round(total_sum, 2)
    print(f"Сума на рахунку через {years} років: {total_amount}")
    return total_amount

deposit = float(input("Введіть розмір початкового вкладу: "))
period = int(input("Введіть тривалість вкладу у роках: "))
rate_input = (input("Введіть відсоткову ставку (default 10%): "))

if rate_input == "":
    rate = 10
else:
    rate = float(rate_input)

result = bank(deposit, period, rate)


''' HT #08
1. Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100),
 кожен елемент якого буде ділитись без остачі на 5 але не буде ділитись на 3.
   Результат: [5, 10, 20, 25, 35, 40, 50, 55, 65, 70, 80, 85, 95]'''


result = [x for x in range(0, 101) if x % 5 == 0 and x % 3 != 0]
print(result)
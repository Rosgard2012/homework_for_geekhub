'''3. Створіть клас в якому буде атребут який буде рахувати кількість
 створених екземплярів класів.'''


class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1


obj1 = MyClass()
print(obj1.count)

obj2 = MyClass()
print(obj2.count)

obj3 = MyClass()
print(obj3.count)

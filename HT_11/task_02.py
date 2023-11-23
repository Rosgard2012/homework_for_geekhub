"""2. Створити клас Person, в якому буде присутнім метод __init__ який буде
 приймати якісь аргументи, які зберігатиме в відповідні змінні.
- Методи, які повинні бути в класі Person - show_age, print_name,
show_all_information.
- Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть
 атребут profession (його не має інсувати під час ініціалізації)."""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_age(self):
        return f"{self.name} is {self.age} years old."

    def print_name(self):
        return f"The name is {self.name}."

    def show_all_information(self):
        return f"Name: {self.name}, Age: {self.age}"


person1 = Person("Alisa", 30)
person2 = Person("Borisa", 25)


person1.profession = "PM"
person2.profession = "QA"


print(person1.show_age())
print(person2.show_age())
print(person1.print_name())
print(person2.print_name())
print(person1.show_all_information())
print(person2.show_all_information())
print(person1.profession)
print(person2.profession)

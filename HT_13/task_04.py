'''4. Create 'list'-like object, but index starts from 1 and index of 0
raises error. Тобто це повинен бути клас, який буде поводити себе так,
 як list (маючи основні методи), але індексація повинна починатись із 1'''


class CustomList:
    def __init__(self, *args):
        self._data = list(args)

    def __getitem__(self, index):
        if index < 1:
            raise IndexError("Index must be greater than 0")
        return self._data[index - 1]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return repr(self._data)

    def append(self, value):
        self._data.append(value)

    def pop(self):
        return self._data.pop()


custom = CustomList(10, 20, 30)
print(custom[1])
print(len(custom))
custom.append(40)
print(custom)
print(len(custom))
print(custom.pop())
print(custom)

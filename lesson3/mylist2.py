"""
Напишите класс MyList2, который будет работать аналогично встроенному классу list(). Класс должен иметь следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __iter__(self): магический метод, который возвращает итератор;
- __next__(self): магический метод, который возвращает следующий элемент последовательности;
- __getitem__(self, index): магический метод, который позволяет обратиться к элементу списка по индексу.
"""


class MyList2:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self):
        if self.counter == len(self.data) - 1:
            raise StopIteration
        self.counter += 1
        return self.data[self.counter]


    def __getitem__(self, index):
        return self.data[index]


# код для проверки 
my_list = MyList2([1, 2, 3])
for i in my_list:
    print(i)  # 1 2 3

print()

# код для проверки
my_list2 = MyList2([1, 2, 3, 4, 5])
for i in my_list2:
    print(i)  # 1 2 3 4 5

print()

print(my_list[1])  # 2

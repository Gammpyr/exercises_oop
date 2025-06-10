"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""
from datetime import datetime


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        if year <= datetime.today().year:
            self.year = year
        else:
            raise Exception('Эта машина еще не была выпущена')


# код для проверки
car = Car('Toyota', 'Corolla', 2022)

car2 = Car('Toyota', 'Corolla', 3000)
# raises Exception('Эта машина еще не была выпущена')

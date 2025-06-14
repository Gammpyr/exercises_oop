"""
Напишите класс Person, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя и возраст человека
- display(self): метод, выводящий на экран имя и возраст человека
- from_birth_year(cls, name, birth_year): класс-метод, принимающий имя и год рождения человека и
возвращающий объект класса Person;
- is_adult(cls, age): статический метод, принимающий возраст человека и возвращающий True,
если он старше 18 лет, и False в противном случае
"""
from datetime import datetime, date


class Person:

    __name: str
    __age: int

    def __init__(self, name , age):
        self.__name = name
        self.__age = age

    def display(self):
        print(f'{self.__name} is {self.__age} years old')


    @classmethod
    def from_birth_year(cls, name, birth_year):
        cur_date = date.today()
        person_age = cur_date.year - birth_year
        return Person(name, person_age)

    @staticmethod
    def is_adult(age):
        return True if age >= 18 else False


# код для проверки 
person1 = Person("John", 28)
person1.display()  # John is 28 years old

person2 = Person.from_birth_year("Mike", 1999)
person2.display()  # Mike is 26 years old

print(Person.is_adult(20))  # True
print(Person.is_adult(15))  # False

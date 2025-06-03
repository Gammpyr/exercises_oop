"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
import time


class Timer:

    def __init__(self):
        self.__elapsed_time = 0

    @property
    def elapsed_time(self):
        return self.__elapsed_time

    def __enter__(self):
        self.__start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__end_time = time.time()
        self.__elapsed_time = self.__end_time - self.__start_time

with Timer() as timer:
    time.sleep(2)

# код для проверки
print("Execution time:", timer.elapsed_time)

# Домашнее задание по теме "Потоки на классах"
# Задача "За честь и отвагу!"
from threading import Thread
import time
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        self.kname = name # имя рыцаря. (str)
        self.power = power # сила рыцаря. (int)
        super().__init__()
# метод run, в котором рыцарь будет сражаться с врагами
    def run(self):
        print(f'{self.kname}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            sleep(1)
            days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f'{self.kname} сражается {days} суток, осталось {enemies} воинов врага.')
        print(f'{self.kname} одержал победу спустя {days} дней(я)!')

# Алгоритм выполнения кода
# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончены!')

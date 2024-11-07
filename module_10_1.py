# Домашнее задание по теме "Введение в потоки".
# Задача "Потоковая запись в файлы"
import time
from time import sleep
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")

time_start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_stop = time.time()
time_result = time_stop - time_start
print("Время выполнения функций:", time_result)

time_start_2 = time.time()
thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))
thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_stop_2 = time.time()
time_result_2 = time_stop_2 - time_start_2
print("Время выполнения функций:", time_result_2)
# task6
'''
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
'''
from itertools import count, cycle
import argparse

def counter()
for number in count(5):
    if number > 20:
        break
    else:
        print(number)

parser = argparse.ArgumentParser (description = 'Скрипт для итератора, генерирующего целые числа, начиная с указанного'
                                                '\n и Скрипт итератор, повторяющий элементы некоторого списка,'
                                                ' определенного заранее.')
parser.add_argument ('start_number', type = int, help = 'начальное значение генератора, целое число')
parser.add_argument ('end_number', type = int, help = 'конечное значение генератора, целое число')
parser.add_argument ('work_list', type = str, help = 'Строка списка, введите значение в кавычках')
args = parser.parse_args ()
print (f'Введеные данные: {args.start_number} , {end_number}, \n {work_list} ')


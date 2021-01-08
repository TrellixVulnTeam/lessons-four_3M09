# task2
'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''
import random

original_list = [element for element in range(random.randint(1, 1000))]
random.shuffle(original_list)
print(original_list)
modifited_list = [element for count, element in enumerate(original_list[1:]) if element > original_list[count]]
print(modifited_list)
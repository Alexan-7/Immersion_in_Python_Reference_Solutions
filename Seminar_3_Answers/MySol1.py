"""
✔ Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
"""

'''Первое решение'''
lst = [4, 4, 3, 5, 1]
print(lst)
print(list(set(lst))) # Класс set (множество) — это одна из ключевых структур данных в Python

'''Второе решение'''
new_lst = []
for el in lst:
    if el not in new_lst:
        new_lst.append(el)
print(sorted(new_lst, reverse=True))

'''List compehension'''
new_lst = [el for el in lst if el not in new_lst]
print(new_lst)
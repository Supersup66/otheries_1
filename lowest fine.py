"""Находит количество элементов меньше, чем заданное и создает список
ВАЖНО! В отсортированном списке - индекс элемента - равен количеству элементов
меньше него. Решение задачи "в лоб" O(n^2).
Здесь сложность линеаризованная - O(n log n)"""

# Превращает введенную строку '1 2 3 4' в list[int]
rad_ind = [int(x) for x in input().split()]
sorted_mas = sorted(rad_ind)
for num in rad_ind:
    print(''.join(str(sorted_mas.index(num))), end=' ')

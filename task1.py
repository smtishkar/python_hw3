# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]


my_list = [1, 2, 3, 1, 2, 4, 5]
new_list = []

for elem in my_list:
    if my_list.count(elem) > 1:
        new_list.append(elem)
print(list(set(new_list)))


# Вариант 2

new_list2 = []
for elem in new_list:
    if elem not in new_list2:
        new_list2.append(elem)
print(new_list2)

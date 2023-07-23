# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно
#  вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
from itertools import permutations

my_dict = {'котелок': 3, 'палатка': 7, 'плитка': 4, 'посуда': 3, 'удочка': 4, 'книги': 3, 'топор': 5}
MAX_CAPACITY = 15
weight = 0

# Первый вариант

# print('С собой можно взять следующие вещи:')
# for things, values in my_dict.items():
#     weight += my_dict[things]
#     if weight <= MAX_CAPACITY:
#         print(f"{things} - {values} кг")
          

#Второй вариант. Поиск всех возможных вариантов
my_things_list = []
new_list = []
common_list=[]
final_list = []

for keys in my_dict.keys():
    my_things_list.append(keys)

weight = 0 
for things in permutations(my_things_list,len(my_things_list)):
    weight = 0 
    for i in things:
        a = my_dict.get(i)
        weight += my_dict.get(i)
        if weight <= MAX_CAPACITY:
            new_list.append(i)

    temp = new_list.copy()
    common_list.append(temp)
    new_list.clear()

for elem in common_list:
    if elem not in final_list:
        final_list.append(elem)

for i, elem in enumerate(final_list, start=1):
    print(f"Вариант {i} - {elem}")

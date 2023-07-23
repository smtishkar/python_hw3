# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно
#  вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.


my_dict = {'котелок': 3, 'палатка': 7, 'плитка': 4, 'посуда': 3, 'удочка': 4, 'книги': 3, 'топор': 5}
MAX_CAPACITY = 15
weight = 0

# Первый вариант

print('С собой можно взять следующие вещи:')
for things, values in my_dict.items():
    weight += my_dict[things]
    if weight <= MAX_CAPACITY:
        print(f"{things} - {values} кг")
          

#Второй вариант
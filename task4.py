# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# * Какие вещи взяли все три друга
# * Какие вещи уникальны, есть только у одного друга
# * Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# * Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.


dict_frends_atribute = {"Алексей": ("мяч", "посуда", "котелок",),\
                        "Витя": ("вода", "мяч", "котелок",),\
                        "Сергей": ("плитка", "котелок", "мангал",),\
                         "Коля" :  ("ружье", "уголь", "мясо",)   }

friend_list = []
all_things = []
unique_things = []
temp_except=[]
absent_things = []

for keys in dict_frends_atribute:
   friend_list.append(keys)

# Формируем список всех вещей
for keys, values in dict_frends_atribute.items():
    all_things = set(all_things).union(set(dict_frends_atribute[keys]))
print(f"Все друзья взяли с собой - {all_things}")


# Формируем список уникальных вещей у каждого друга
for keys, values in dict_frends_atribute.items():
    for i in friend_list:
        if i != keys:
            temp_except = set(temp_except).union(set(dict_frends_atribute[i]))
    unique_things = set(dict_frends_atribute[keys]).difference(temp_except)
    print(f" Уникальная вещь для {keys} - {unique_things}")
    temp_except.clear()
    unique_things.clear()


# Формируем список вещей которые есть у всех, но нет у одного друга
for keys, values in dict_frends_atribute.items():
    for i in friend_list:
        if i != keys:
            temp_except = set(temp_except).union(set(dict_frends_atribute[i]))
    absent_things = temp_except.difference(set(dict_frends_atribute[keys]))
    print(f" У {keys} нет следующих вещей - {absent_things}")
    temp_except.clear()
    absent_things.clear()

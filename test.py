from itertools import permutations

my_dict = {'котелок': 3, 'палатка': 7, 'плитка': 4, 'посуда': 3, 'удочка': 4, 'книги': 3, 'топор': 5}

a = []
for keys in my_dict.keys():
    a.append(keys)

print(a)

my_things_list = ['котелок', 'палатка', 'плитка', 'посуда', 'удочка', 'книги', 'топор']

new_list = []
common_list=[]
final_list = []

weight = 0 
for thingS in permutations(my_things_list,7):
    weight = 0 
    for i in thingS:
        a = my_dict.get(i)
        weight += my_dict.get(i)
        if weight <=15:
            new_list.append(i)

    temp = new_list.copy()
    common_list.append(temp)
    new_list.clear()

for elem in common_list:
    if elem not in final_list:
        final_list.append(elem)

# for i, elem in enumerate(final_list, start=1):
#     print(f"Вариант {i} - {elem}")

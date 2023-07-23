my_list = [[1,2,3],[1,2,3]]
# print(frozenset(my_list))
a = []
for i in my_list:
    if i not in a:
        a.append(i)

print(a)
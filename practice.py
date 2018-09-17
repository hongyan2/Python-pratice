list1 = [2, 3, 8, 4, 9, 5, 6]
list2 = [5, 6, 10, 17, 11, 2]
list3 = list1 + list2
print (set(list3))

list = []
for x in list3:
    if x not in list:
        list.append(x)
list.sort()
print (list)
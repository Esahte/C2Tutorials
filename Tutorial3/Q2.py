list1 = '1 2 3 2 1 6 3 4 5 2'.split()
list2 = []

for i in list1:
    list1.sort()
    for x in list2:
        if i == x:
            list2.remove(i)

    list2.append(i)

print(f'The distinct numbers are: {list2}')

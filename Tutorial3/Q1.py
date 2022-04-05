# list1 = []
# x = int(input('Enter a number to go up to: '))
# for i in range(0, x):
#     t = int(input('Enter a number between 1 and 100: '))
#     list1.append(t)
list1 = [x for x in (str(input('Enter a list of numbers from 1 to 100: ')).split())]

list2 = []
list1.sort()
for i in list1:
    for x in list2:
        if i == x:
            list2.remove(i)

    list2.append(i)

for i in list2:
    if list1.count(i) >= 2:
        print(f'{i} occurs {list1.count(i)} times')
    else:
        print(f'{i} occurs {list1.count(i)} time')

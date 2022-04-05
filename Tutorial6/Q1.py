from Stack import Stack


m = []
a = Stack()
for i in range(2, 100):
    for j in range(1, 100):
        if i % j == 0:
            m.append(j)
    if len(m) <= 2:
        a.push(i)
    m.clear()
while not a.isEmpty():
    print(a.pop(), end=' ')

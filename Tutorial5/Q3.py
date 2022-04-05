y = input('Enter numbers: ')
i = y.split()
num = [int(x) for x in i]

lSC = 0
lSI = 0

cLSC = 0

p = num[0]
for index in range(len(num)):
    numIn = num[index]
    if numIn == p:
        cLSC += 1
    elif cLSC > lSC:
        lSC = cLSC
        lSI = index - cLSC
        cLSC = 1

    p = num[index]

print(f'the longest same number sequence starts at index {str(lSI)} with '
      f'{str(lSC)} values of {str(num[lSI])}')

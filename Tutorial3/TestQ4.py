from Q4 import shuffle


def main():
    a = int(input('Enter how many numbers u want: '))
    lst = []
    for i in range(0, a):
        b = int(input('Enter a number: '))
        lst.append(b)
    print(shuffle(lst))


main()

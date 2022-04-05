def indexOfSmallestElement(lst):
    x = min(lst)
    if len(lst) > 1:
        return lst.index(x)
    return lst.index(x)


def main():
    print(indexOfSmallestElement([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


main()


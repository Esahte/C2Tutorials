def shuffle(lst):
    x = lst
    n = []
    x.reverse()
    for i in x:
        n.append(i)
        x.remove(i)
        for t in x:
            n.append(t)
            x.remove(t)
            continue
    n.extend(x)
    return n

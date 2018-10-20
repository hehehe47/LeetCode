def sorta(A):
    o, e = [], []
    for i in A:
        if i % 2 == 0:
            e.append(i)
        else:
            o.append(i)
    return e + o


print(sorta([3, 1, 2, 4]))

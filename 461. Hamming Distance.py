def hamming(x, y):
    count = 0
    while x != 0 or y != 0:
        if x != 0 and y != 0:

            if x % 2 != y % 2:
                count += 1
            x = int(x / 2)
            y = int(y / 2)
        elif x == 0:
            if y % 2 != 0:
                count += 1
            y = int(y / 2)
        elif y == 0:
            if x % 2 != 0:
                count += 1
            x = int(x / 2)

    return count


print(hamming(1, 4))

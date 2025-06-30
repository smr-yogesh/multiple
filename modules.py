def findMultiple(a, b, c):
    y = []
    for x in range(1, c):
        if (x % a) == 0:
            y.append(x)
        if (x % b) == 0:
            y.append(x)
    z = []
    z.append(y[0])

    for x in range(len(y) - 1):
        if y[x] != y[x + 1]:
            z.append(y[x + 1])

    return (c, ":", " ".join(map(str, z)), "\n")

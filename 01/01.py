data = [int(l) for l in open("input.txt").readlines()]


def fuel(m):
    f = m // 3 - 2
    return f if f <= 0 else f + fuel(f)


result = sum(map(fuel, data))

print(result)

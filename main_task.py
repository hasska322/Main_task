from random import randint


n = randint(1, 100000)
target = randint(1, n)
print("n =", n, "target =", target)


def result():
    res = 0
    ideal = 0
    for i in range(1, n + 1):
        if i == target:
            res += 90/i
            continue
        res += 100 / i

    for i in range(1, n + 1):
        ideal += 100 / i

    return round(100 / ((ideal - res) * 10))


print(result())



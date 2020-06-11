from random import randint


n = randint(1, 100000)
target = randint(1, n)

print("n =", n, "target =", target)


def result():
    res = sum([(100 / i) if i != target else 90 / i for i in range(1, n + 1)])
    ideal = sum([100 / i for i in range(1, n + 1)])

    return round(10 / (ideal - res))


print(result())



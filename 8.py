import random


def add_to(a):
    c = 1
    while (c < a):
        c *= 2

    return c


n = random.randint(0, 10000)

arr = [random.randint(0, 100000) for _ in range(n)]

print(f"Было составлен массив из {n} элементов/a, было добавлено {add_to(n) - n}")

arr += [0] * (add_to(n) - n)
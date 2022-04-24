def extra_enumerate(x):
    sum_current = 0
    for i in range(0, len(x)):
        sum_current += x[i]
        frac = sum_current / sum(x)
        yield i, x[i], sum_current, frac


x = [1, 3, 4, 2]

for i, elem, s, frac in extra_enumerate(x):
    print(elem, s, frac)
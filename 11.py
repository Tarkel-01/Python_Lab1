import decimal


def frange(a, b, c):
    while (a <= b):
        yield a
        a += c


for x in frange(1, 5, decimal.Decimal('0.1')):
    print(x)
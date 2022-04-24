bank = {1000: 100, 500: 100, 100: 100, 50: 100, 10: 100, 1: 100}
ans = {}

n = int(input())

for val in bank.keys():
    while n >= val and bank[val] > 0:
        n -= val
        bank[val] -= 1
        ans[val] = ans.get(val, 0) + 1

if n == 0:
    print(" + ".join([f"{ans[key]}*{key}" for key in ans.keys() if ans[key] != 0]))
else:
    print('Невозможно выполнить данную операцию!!!')
ans = dict()

for i in input():
    ans[i] = ans.get(i, 0) + 1

print(*[i for i in ans.keys() if ans[i] == 1])

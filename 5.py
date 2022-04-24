ans = str()
for elem in input().split():
    if (elem[0].isupper()):
        ans += elem.upper()
    else:
        ans += elem
    ans += ' '
print(ans)

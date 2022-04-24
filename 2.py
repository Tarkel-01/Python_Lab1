arr = [int(x) for x in input().split()]

print("True" if arr == sorted(arr) else "False")
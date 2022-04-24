lvl = set()
for char in input():
    if char.isdigit():
        lvl.add(1)
    elif char.isupper():
        lvl.add(2)
    elif char.islower():
        lvl.add(3)
    else:
        lvl.add(4)
if len(lvl) < 2:
    print("Очень слабый пароль!!!")
elif len(lvl) == 2:
    print("Слабовато :(")
elif len(lvl) == 3:
    print("фифти - фифти")
else:
    print("Нормас :)")
num = float(input())

if (num < 0.0):
    print("Некорректный формат!!!")
else:
    str_num = f"{int(num)} руб. {int((num - int(num)) * 100)} коп."
    print(str_num)
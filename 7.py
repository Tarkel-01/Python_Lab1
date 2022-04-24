adress_list = ['www.yandex.ru', 'www.google.com', 'amazon.com']

tmp1 = ['http://' + i for i in adress_list if i.find('www', 0, 3) == 0]
tmp2 = [i for i in adress_list if i.find('www', 0, 3) != 0]
tmp1 = [i + '.com' for i in tmp1 if i[-4:] != '.com'] + [i for i in tmp1 if i[-4:] == '.com']

adress_list = tmp1 + tmp2
print(adress_list)
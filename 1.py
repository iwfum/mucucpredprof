import csv

with open('products.csv', encoding='utf-8-sig') as f, open('products_new.csv', 'w', newline='', encoding='utf-8-sig') as nf:
    data = list(csv.reader(f, delimiter=';'))
    print(*data)
    # prodano = 0
    # k = 0
    # average_price = 0
    # category = 'Закуски'
    # data1 = list(csv.reader(nf, delimiter=';'))
    # print(data1)
    # for i in data:
    #     if i[0] == category:
    #         prodano += int(i[4])
    #         k += 1
    #         average_price += int(i[3])
    #         average = average_price // k
    #         last = (str(average*prodano))
    #         print(f' Итоговая сумма  по категории Закуски равна {last}')
    # result = csv.writer(nf, delimiter=';')
    # for i in data:
    #     if i[5] == '':
    #         i[5] = i[3] * int(i[4])
    #csv.writer()

    # print(result)
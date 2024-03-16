import csv

#считаем данные с файла и зададим их в переменную
with open('products.csv', encoding='utf-8-sig') as f:
    data = list(csv.reader(f, delimiter=';'))
    category = input()
    flag = False
    #зададим условия выполнения поиска
    while category != 'молоко':
        for i in data:
            if category == i[0]:
                if i[4] == min(i[4]):
                    print(f'В категории: {i[0]} товар: {i[1]} был куплен {(i[4])} раз')
                    flag = True
                    break
        if not flag:
            print('Такой категории не существует в нашей БД')
        flag = False
        category = input()
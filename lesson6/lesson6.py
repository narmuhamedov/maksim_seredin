#анонимные функции исключения
#try except
while 1:
    try:
        first_number = float(input('Введите первое число '))
        operations = str(input('Выберите действие + - * /'))
        second_number = float(input('Введите второе число '))
    except:
        print('Введите пожалуйста цифры')
        continue

    if operations == '+':
        result = first_number+second_number
        print(f'Ответ - {result}')

    elif operations == '-':
        result = first_number - second_number
        print(f'Ответ - {result}')


    elif operations == '*':
        result = first_number * second_number
        print(f'Ответ - {result}')


    elif operations == '/':
        result = first_number / second_number
        print(f'Ответ - {result}')

    else:
        print('Что то пошло не так вы хотите продолжить? 1-да 2-нет')
        a = str(input('1-да 2-нет '))
        if a == '1':
            continue
        elif a == '2':
            break
        else:
            print('Прога сломана пока!!!')
            break


# try:
#     a = 12
#     b = 12
#     print(a+b)
# except:
#     print(f'Это ошибка число со строкой складывать нельзя')

#sorted
# words = ['date', 'apples', 'names', 'boolean', 'python', 'integer']
# s_words = sorted(words, key=lambda x: len(x))
# print(s_words)

#filter
# word = ['apple', 'banana', 'orange']
# a = list(filter(lambda x: len(x)<=5, word))
# print(a)

#map
# numbers = [1, 2, 3, 4, 5]
# plus = list(map(lambda x: x**2, numbers))
# print(plus)

# plus = lambda x, y: x+y
# print(plus(1, 3))
#
#
#
# def plus(x,y):
#     return x+y
#     return x*y
#
# print(plus(10,5))

#ex1
univer = []
kollege = []
army = []
married = []

abiturients = [
    {'name': 'Саша', "ОРТ": 120, 'gender': 'male'},
    {'name': 'Маша', "ОРТ": 87, 'gender': 'female'},
    {'name': 'Игорь', "ОРТ": 98, 'gender': 'male'},
    {'name': 'Антон', "ОРТ": 109, 'gender': 'male'},
    {'name': 'Вика', "ОРТ": 50, 'gender': 'female'},
    {'name': 'Денис', "ОРТ": 30, 'gender': 'male'}
]

def all_abit(lst):
    for i in lst:
        for keys, values in i.items():
            print(f'{keys}-{values}')


def selection(lst, univer:list,kollege:list, army:list, married: list):
    for i in lst:
        if i['ОРТ'] >= 110:
            univer.append(i)
        elif i['ОРТ']<=110 and i['ОРТ']>=80:
            kollege.append(i)

        elif i['ОРТ'] < 80 and i['gender']=='male':
            army.append(i)

        elif i['ОРТ'] < 80 and i['gender'] == 'female':
            married.append(i)

selection(abiturients, univer, kollege, army, married)
print('-'*10)
print(f'В универ пошли - {univer}\n'
      f'В колледж пошли - {kollege}\n'
      f'В армию пошли - {army}\n'
      f'Замуж вышли - {married}')



#all_abit(abiturients)


#функции - формула как в математике
#
# def menu(**kwargs):
#     return kwargs
#
# monday = menu(utro='Яйичница', obed='Борщ', uzin='рыба')
# monday.update(night='tea')
# print(monday)



#*args - преобразовывает в кортеж  **kwargs-преобразовывает в словарь
# def average(*temperatur):
#     return sum(temperatur)/len(temperatur)
#
#
# oblast = average(float(input()), float(input()), float(input()))
# #print(f'Среднее значение всех областей температуры = {round(oblast, 2)}')






#return в функциях
# def greenting(name):
#     return f'Привет что делаешь? - {name}'
#
# print(greenting(input('Имя? ')))
# # greenting(input(''))

# while 1:
#     def greeting(name):
#         print(f'Привет что нового у тебя {name}')
#
#     greeting(str(input('Как вас зовут?')))



#параметры по умолчанию указывается всегда в конце
# def square1(a, b, c=12):
#     print(a+b/c)
#
# square1(10,22)


#Обычная классическая функция
# def square(a, b):
#     print(a*b)
#
# square(1, 3)
# square(3,4)
# square(12,23)




# a = 12
# b = 32
# c = 123
# v = 32
# print(a+b)
# print(a+b)


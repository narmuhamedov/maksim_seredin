# #Модули в python
import turtle
t = turtle.Turtle()

for _ in range(4):
    t.forward(100)
    t.right(90)


turtle.done()


# import random
# import time
# from random import randint
# import datetime
#
# cash = 500
# start = datetime.datetime.now()
# while cash !=0:
#     try:
#         bet = int(input(f'Введите вашу ставку\nДоступно - {cash} '))
#         if bet>cash:
#             print(f'Введите правильно ставку у вас доступно {cash}')
#             continue
#         comp = [randint(1, 6), randint(1, 6)]
#         user = [randint(1, 6), randint(1, 6)]
#     except:
#         print('Пожалуйста вводите только цифры')
#         continue
#     if sum(comp)>sum(user):
#         cash -= bet
#         print(f'You lose\n'
#               f'Вы хотите продолжить? ')
#         a = str(input('да нет'))
#         if a=='да':
#             continue
#         else:
#             break
#
#
#     elif sum(comp)<sum(user):
#         cash+=bet
#         print('You Win')
#         a = str(input('да нет'))
#         if a == 'да':
#             continue
#         else:
#             break
#
#     else:
#         print('Ничья')
#         a = str(input('да нет'))
#         if a == 'да':
#             continue
#         else:
#             break
#
# time_ = datetime.datetime.now()-start
# print(time_)
#
#
#
#
#
#
#
# # def greeting(name, age):
# #     return f'Привет {name} тебе {age} лет'

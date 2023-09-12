with open('game.txt', 'r')as file:
    print(file.read())






# import time
# from random import randint
# import datetime
#
# cash = 500
# start = datetime.datetime.now()
# while cash !=0:
#     try:
#         bet = int(input(f'Введите вашу ставку\nДоступно - {cash} '))
#
#         if bet > cash:
#             print(f'Введите правильно ставку у вас доступно {cash}')
#             continue
#
#         comp = [randint(1, 6), randint(1, 6)]
#         user = [randint(1, 6), randint(1, 6)]
#     except:
#         print('Пожалуйста вводите только цифры')
#         continue
#
#     with open('game.txt', 'a')as file:
#         file.write(f'у вас доступно - {cash}\n'
#                    f'Вы внесли - {bet}\n')
#
#     if sum(comp)>sum(user):
#         cash -= bet
#         print(f'You lose')
#         with open('game.txt', 'a')as file:
#             file.write(f'comp - {sum(comp)}\n'
#                        f'user - {sum(user)}\n'
#                        f'You lose\n')
#         print('Продолжить?')
#         a = str(input('да нет'))
#         if a == 'да':
#             continue
#         else:
#             break
#
#
#
#     elif sum(comp)<sum(user):
#         cash+=bet
#         print('You Win')
#         with open('game.txt', 'a')as file:
#             file.write(f'comp - {sum(comp)}\n'
#                        f'user - {sum(user)}\n'
#                        f'You win\n')
#         print('Продолжить?')
#         a = str(input('да нет'))
#         if a == 'да':
#             continue
#         else:
#             break
#
#     else:
#         print('Ничья')
#         with open('game.txt', 'a')as file:
#             file.write(f'comp - {sum(comp)}\n'
#                        f'user - {sum(user)}\n'
#                        f'Draw\n')
#         print('Продолжить')
#         a = str(input('да нет'))
#         if a == 'да':
#             continue
#         else:
#             break
#
#
#
# time_ = datetime.datetime.now()-start
# print(time_)
# with open('game.txt', 'a')as file:
#     file.write(f'общее время игры - {time_}')
#
#

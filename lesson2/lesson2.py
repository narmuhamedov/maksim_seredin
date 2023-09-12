#Цикли и условные операторы

#Циклы while for
# for i in range(1, 100):
#     print(i)

#Цикл for работает только 1 раз он начал и он сразу же закончен


#Цикл while работает бесконечно до тех пор пока значение не станет ложью.

# дано 40 бутылок кока колы нужно распедилить по коробкам 0.5л - 1л - 1.5л
#вывести колличество бутылок 0.5л - 1л - 1.5л




#Пример с яблоками
apple = 10
good_apples = 0
bad_apples = 0

while apple !=0:
    question = int(input('Это хорошее или плохое яблоко? 1-хорошее 2-плохое '))
    if question == 1:
        apple -= 1
        good_apples +=1
        print(f'Сейчас хороших яблок - {good_apples}\nСейчас в коробке - {apple}')

    elif question == 2:
        apple -= 1
        bad_apples +=1
        print(f'Сейчас плохих яблок - {bad_apples}\nСейчас в коробке - {apple}')

print(f'Итог-(хороших яблок) - {good_apples}\n(плохих яблок)-{bad_apples}')




# name = str(input('Как вас зовут'))
# while 1:
#     print(name)



#условные операторы -> if elif else

#==, <=, >=,!/ or and not
#с 23 июля по 22 августа,
# day = int(input('Введите дату рождения! '))
# month = int(input('Введите месяц рождения! '))
# if day>=23 and month==7 and day<=31 or day<=22 and month==8 and day<=31:
#     print('Вы лев')
# else:
#     print('вы не лев')


#
# number = int(input('Введите балл за тест: '))
# if number >= 90:
#     print(f'Отлитный результат')
# elif number <= 89 and number >= 79:
#     print(f'Хороший результат')
# elif number <= 78 and number >= 60:
#     print(f'Удовлетворительный результат')
# elif number <= 59:
#     print('Вы завалили тест')





# name = str(input('Как вас зовут? '))
# if name == "Максим":
#     print(f'Привет {name} вы ученик')
# elif name == 'Радомир':
#     print(f'Привет {name} вы преподаватель')
# else:
#     print(f'Привет {name} вы другой человек!')
#

#Светофор
# color = str(input('Какой цвет горит? '))
# if color == 'red':
#     print(f'Горит {color} STOP!')
# elif color == 'yellow':
#     print(f'Горит {color} READY!')
# elif color == 'green':
#     print(f'Горит {color} GO!')
# else:
#     print('Смотри по ситуации!')
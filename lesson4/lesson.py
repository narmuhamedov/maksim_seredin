#словари и сеты
#
# #Сеты - структура данных
# shaverma = {'Лаваш', 'Мясо', 'Картошка фри', "Помидоры", "Огурцы", "Морковь"}
# shashlyk = {"Лаваш", "Мясо", "Помидоры", "Лук маринованный", "Укус", "Соус"}
#
# #Похожие значения
# print(shaverma.intersection(shashlyk))
# #Микс значений
# print(shaverma.union(shashlyk))
# #Вывод непохожих ингридиентов
# print(shaverma.symmetric_difference(shashlyk))
#
# #Преобразования списка в сет
# list_1 = [1,3,4,5,6,7]
# list_1 = set(list_1)
# print(list_1)



#У словарей есть ключ и значени (Примечание ключи должны быть уникальными -
# значения могут быть разными
# ключ и значение могут быть любого типа данных
# student = {
#     'name': "Ivan",
#     'age': 26,
#     True: 'education',
#     1.85: 'height',
#     1997: 'cow',
#     False: False,
#     2020: 1997
# }
# print(student['name'])
# print(student)
#Изменять добавлять и удалять
#добавление
# student['auto'] = "Volkswagen"
# print(student.values())
# print(student.keys())

#Изменение
# student[2020] = 1990
# print(student)

#Удаление
# del student[2020]
# print(student)

#Вертикальный вид(Преобразования пар и ключей)
# for i, j in student.items():
#     print(f'{i} - {j}')

#Преобразования 2х списков в словарь
# nominal = [1, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
# person = ['монета', 'монета', 'монета', 'монета', 'Тоголок Молдо', "ДАтка", 'Сатылганов',
#           'Осмонов', "Каралаев", 'person1000', 'person2000', 'person5000'
#           ]
# banknotes = dict(zip(nominal, person))
# for i,j in banknotes.items():
#     print(i,j)
# print(banknotes)
#
# persons = dict(car=1997, name='Golf4', akkp = 'qwerty')
# persons.update(car=2000)
# persons.update(color='black')
# print(persons)
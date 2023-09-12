#списки и кортежи
#Кортежи
data_types = (1, 3, 'qwerty', 32)
data_types = list(data_types)
data_types.append('qwenjoqjwe')
data_types = tuple(data_types)
print(data_types)

#Реверсация
a = 'qwerty'
a = list(a)
a.reverse()
print(a)

# name = ['Radomir', 'Andrew', 'Dima']
# name2 = ['Maksim', 'Platon', 'Alex']
# #расширение списка другим
# name2.extend(name)
# print(name)
# print(name2)

#вытаскивание элементов с одного списка и добавление к другому
# all_elements = [1, "qwerty", 22, 12, 'ass', 'qweqwe', True, False]
# all_elements2 = []
# all_elements2.append(all_elements.pop(1))
# all_elements2.append(all_elements.pop(2))
# print(all_elements)
# print(all_elements2)



# numbers = []
# strings = []
# for i in all_elements:
#     if type(i) == str:
#         strings.append(i)
#     elif type(i)==bool:
#         strings.append(i)
#     else:
#         numbers.append(i)

# print(strings)
# print(numbers)



# numbers = [222,11,1,3,2,4,55,12,4324,332,22,1,2]
# numbers.sort()
# print(numbers)

# data_name = "Максим изучает Python"
# data_name = list(data_name)
# data_name.append(1234)
# print(data_name)

#Списки можно добавлять изменять и удалять
#data_types = ['python', 123, 'java', 321, 12.33, 22.22, 123, 123]

#подсчет элементов
#print(data_types.count(123))

#просмотр индекса элемента
#print(data_types.index(123))

#изменение
# data_types[0] = 'Maksim'
# data_types[1] = 1997

#Удаление
# data_types.remove('java')
# del data_types[0]


# #добавление
# data_types.append('qwerty')
# data_types.append(1234)
# #2 добавление между элементами
# data_types.insert(1, False)

#print(data_types)
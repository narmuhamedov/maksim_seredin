ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
events = list(filter(lambda x: x % 2 == 0, ten))
step = list(map(lambda x: x**2, events))
print(step)

def index(lst=ten):
    while 1:
        b = input('Введите индекс, или слово exit для выхода')
        if b!='exit':
            try:
                print(lst[int(b)])
            except:
                print('пож введите индекс от 0 до', len(lst)-1)
                continue
        else:
            break
index()
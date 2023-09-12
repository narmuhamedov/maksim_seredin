#создание первого класса
class Person:
    def __init__(self, name, age, height, hobby, computer, car):
        self.name = name,
        self.age = age,
        self.height = height,
        self.hobby = hobby,
        self.computer = computer,
        self.car = car


    def sing(self, type_song):
        return f'Список песен - {type_song}'


    def __str__(self):
        return (f'Имя-{self.name}\n'
                f'Возраст-{self.age}\n'
                f'Рост-{self.height}\n'
                f'Хобби-{self.hobby}\n'
                f'Комп-{self.computer}\n'
                f'Машина-{self.car}')

human_1 = Person(name='Максим', age=34, height=1.33, hobby='sport', computer=True, car=True)
human_2 = Person(name='Радомир', age=26, height=1.33, hobby='books', computer=True, car=True)
human_3 = Person(name='Иванов', age=40, height=1.33, hobby='sleep', computer=False, car=False)
print(human_1)
print(human_1.sing('рок, попса, шансон'))
print('-'*10)
print(human_2)
print('-'*10)
print(human_3)
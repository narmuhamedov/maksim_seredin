class Car:
    def __init__(self, title, color, volume, year):
        self.title = title
        self.color = color
        self.volume = volume
        self.year = year

    def this_car_can_be_tuning(self, tuning):
        return f'На эту машину можно установить? - {tuning}'



class FuelCar(Car):
    def __init__(self, title, color, volume, year):
        super().__init__(title, color, volume, year)



    def this_car_can_be_gaz(self, volume_gaz):
        return f'На эту машину идет ГБО'


class Electric_Car(Car):
    def __init__(self, title, color, volume, year, game):
        super().__init__(title, color, volume, year)
        self.game = game

    def this_car_can_be_sound(self, sound):
        return f'На эту машину можно установить звуки - {sound}'


class Hybrid_car(FuelCar, Electric_Car):
    def __init__(self, title, color, volume, year, volume_fuel):
        super().__init__(title, color, volume, year, volume_fuel)



hyb = Hybrid_car(title=True, color=True, volume=True, year=False, volume_fuel=True)













# class Father:
#     def __init__(self, eyes, brown, height, web, harackter, work):
#         self.eyes = eyes
#         self.br = brown
#         self.ht = height
#         self.web = web
#         self.hr = harackter
#         self.work = work
#
#     def can_be_teacher(self, learning):
#         return f'father can be {learning}'
#
#
# class Monther:
#     def __init__(self, cooking, cleaner, read_fairytail):
#         self.c = cooking
#         self.cl = cleaner
#         self.rf = read_fairytail
#
#
#     def can_be_cook(self, ingridients):
#         return f'Mother can be learning cooking with this {ingridients}'
#
#
# class Child(Father, Monther):
#     def x(self):
#         return (f'{self.eyes}\n'
#                 f'{self.br}\n'
#                 f'{self.ht}\n'
#                 f'{self.web}\n'
#                 f'{self.hr}\n'
#                 f'{self.work}\n'
#                 f'{self.c}\n'
#                 f'{self.cl}\n'
#                 f'{self.rf}')
#
#
#
# clild = Child()
#
#
# print(clild.x(eyes='Blue', brown='dark', height=13.23, web='instagram', harackter='middle',
#               work=True))
#
# print(clild.can_be_cook('Плов'))
# print(clild.can_be_teacher('Пилить доски'))
# print(clild)
#

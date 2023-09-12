import random
import compare

class BlackJack:
    def __init__(self):
        self.card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.player = [random.choice(self.card), random.choice(self.card)]
        self.computer = [random.choice(self.card), random.choice(self.card)]
        self.lose_or_win = [0, 1000, 0]

    def game(self):
        print(f'Доступные действия\n'
              f'2.Draw Card only player\n'
              f'Your Cards{sum(self.player)}\n'
              f'5.Russian Roollet')
        choise = int(input('Выберите действие '))

        while 1:
            compare_1 = compare.CompareCards(player_list=self.player, computer_list=self.computer)
            if choise == 2:
                self.player.append(random.choice(self.card))
                if compare_1.compare_result():
                    break
            elif choise == 5:
                self.computer.append(random.choice(self.lose_or_win))
                self.player.append(random.choice(self.lose_or_win))
                if compare_1.compare_result():
                    break
games = BlackJack()
games.game()

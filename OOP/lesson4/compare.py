class CompareCards:
    def __init__(self, player_list, computer_list):
        self.pl_lst = player_list
        self.cp_list = computer_list

    def compare_result(self):
        if sum(self.pl_lst)>20 and sum(self.cp_list)<20:
            print(f'Our cards: {sum(self.pl_lst)}You win!!!\n'
                  f'Computer result{sum(self.cp_list)}')
            return True

        elif sum(self.pl_lst)<20 and sum(self.cp_list)>20:
            print(f'Our cards: {sum(self.pl_lst)}You Lose!!!\n'
                  f'Computer result{sum(self.cp_list)}')
            return True

        elif sum(self.pl_lst) == 20 and sum(self.cp_list) == 20:
             print(f'Our cards: {sum(self.pl_lst)}Draw!!!\n'
                   f'Computer result{sum(self.cp_list)}')
             return True

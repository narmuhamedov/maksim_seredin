class Russian_lang:
    def __init__(self, text):
        self.txt = text

    def greeting(self):
        return f'Здорова'

class English_lang:
    def __init__(self, text):
        self.txt = text

    def greeting(self):
        return 'Hello'

class Germany_lang:
    def __init__(self, text):
        self.txt = text

    def greeting(self):
        return 'Guten Tag'

russian = Russian_lang(text='Русский')
english = English_lang(text='Английский')
germany = Germany_lang(text='Немецкий')

print(russian.greeting(), english.greeting(), germany.greeting())






# class BankAccount:
#     def __init__(self, login, password, secret_key):
#         self.lg = login
#         #self._ps = password
#         #self.__sc = secret_key
#
#     def balance(self, summary):
#         return f'Summary - {summary}'
#
#     def __str__(self):
#         return (f'{self.lg}\n')
#
# account = BankAccount(login='admin', password=123, secret_key='123fdsfsdf')
# print(account._balance(12345))
# print(account)
# print(account.__sc)
# print(account._ps)
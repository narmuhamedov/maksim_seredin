class JunDev:
    def __init__(self, laptop, salary, programm_lang):
        self.laptop = laptop
        self.salary = salary
        self.prog_lg = programm_lang

    def copy_paste(self, src):
        return f'This proger can copy paste from - {src}'

    def __str__(self):
        return (f'Ноутбук - {self.laptop}\n'
                f'ЗП - {self.salary}\n'
                f'ЯП - {self.prog_lg}')

proger_1 = JunDev(laptop=True, salary=30.000, programm_lang='python')
print(proger_1.copy_paste('Google'))
print(proger_1)
print('-'*10)

class MiddleDev(JunDev):
    def __init__(self, laptop, salary, programm_lang, mentor):
        super().__init__(laptop, salary, programm_lang)
        self.mentor = mentor


    def __str__(self):
        return super().__str__()+f'\nmentor-{self.mentor}'

mid_dev = MiddleDev(laptop=True, salary=50.000, programm_lang='Java,Python',
                    mentor=True)
print(mid_dev.copy_paste('Google'))
print(mid_dev)
print('-'*10)

class SeniorDev(MiddleDev):
    def __init__(self, laptop, salary, programm_lang, mentor, bissness):
        super().__init__(laptop, salary, programm_lang, mentor)
        self.bs = bissness


    def advanced_skills(self, lang):
        if lang == 'python':
            return 'Вы крутой прогер пайтон популярен'
        elif lang == 'java':
            return 'вы не крутой прогер'
        elif lang == 'c++':
            return 'вы олдовый прогер'


    def __str__(self):
        return super().__str__()+f'\nbissnes-{self.bs}'

sen_prog = SeniorDev(laptop=True, salary=130.000, programm_lang='python', mentor=True,
                     bissness=True)
print(sen_prog.advanced_skills(input('LANG?')))
print(sen_prog)
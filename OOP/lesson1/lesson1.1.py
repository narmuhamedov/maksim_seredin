class OldPhone:
    def __init__(self, calling, game, sms, alarm, clock):
        self.calling = calling,
        self.game = game,
        self.sms = sms,
        self.alarm = alarm,
        self.clock = clock

    def unkillable(self, beat_with_a_hammer):
        return f'Били его молотком но не - {beat_with_a_hammer}'

    def __str__(self):
        return (f'Звонки - {self.calling}\n'
                f'Игры - {self.game}\n'
                f'СМС - {self.sms}\n'
                f'Будильник - {self.alarm}\n'
                f'Часы - {self.clock}')

nokia3310 = OldPhone(calling=True, game='snake', sms=True, alarm=True, clock=True)
print(nokia3310)
print(nokia3310.unkillable('разбили'))


class RedmiNote(OldPhone):
    def __init__(self, calling, game, sms, alarm, clock, wifi, bluetooth, nfc):
        super().__init__(calling, game, sms, alarm, clock)
        self.wifi = wifi,
        self.bluetooth = bluetooth
        self.nfc = nfc

    def camera(self, double_cam):
        return f'Есть 2 камеры - {double_cam}'

    def __str__(self):
        return super().__str__()+(f'\nwifi-{self.wifi}\n'
                                  f'блютус-{self.bluetooth}\n'
                                  f'nfc - {self.nfc}')


redmi_note_10 = RedmiNote(calling=True, game='Race', sms=True,alarm=True,clock=True,
                          wifi=True, bluetooth=5.0, nfc=True)
print('-'*10)
print(redmi_note_10)
print(redmi_note_10.unkillable('Били и разбили'))
print(redmi_note_10.camera(True))

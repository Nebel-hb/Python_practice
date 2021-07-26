class Player:
    def battle(self):
        print('...')


class Fighter(Player):
    def battle(self):
        print('slash')


class Wizard(Player):
    def battle(self):
        print('magic')


for p in [Player(), Fighter(), Wizard()]:
    p.battle()

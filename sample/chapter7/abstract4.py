import abc


class Player(abc.ABC):
    @abc.abstractmethod
    def battle(self):
        pass


class Fighter(Player):
    pass


class Wizard(Player):
    def battle(self):
        print('magic')


for p in [Fighter(), Wizard()]:
    p.battle()

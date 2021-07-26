class Player:
    LEVEL_LIMIT = 10

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def display(self):
        print('Name :', self.name)
        print('Level:', self.level)

    def level_up(self, number):
        self.level += number
        self.__check_level()

    def __check_level(self):
        if self.level > Player.LEVEL_LIMIT:
            self.level = Player.LEVEL_LIMIT


class Fighter(Player):
    def __init__(self, name, level, sword):
        Player.__init__(self, name, level)
        self.sword = sword

    def display(self):
        Player.display()
        print('Sword:', self.sword)

    def slash(self):
        print('Slashing!')


class Wizard(Player):
    def __init__(self, name, level, wand):
        Player.__init__(self, name, level)
        self.wand = wand

    def display(self):
        Player.display(self)
        print('Wand :', self.wand)

    def magic(self):
        print('Casting a magic!')


class MagicKnight(Fighter, Wizard):
    def __init__(self, name, level, sword, wand):
        Player.__init__(self, name, level)
        self.sword = sword
        self.wand = wand

    def display(self):
        Player.display(self)
        print('Sword:', self.sword)
        print('Wand :', self.wand)


mk = MagicKnight('Gobou', 3, 'silver', 'glass')
mk.display()
mk.slash()
mk.magic()

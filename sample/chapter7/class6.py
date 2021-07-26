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
        Player.display(self)
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


f = Fighter('Daikon', 1, 'iron')
f.display()
f.slash()

w = Wizard('Ninjin', 2, 'wood')
w.display()
w.magic()

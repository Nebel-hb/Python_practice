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


p1 = Player('Daikon', 1)
p1.level_up(10)
p1.display()

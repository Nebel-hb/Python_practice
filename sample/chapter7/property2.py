class Player:
    LEVEL_LIMIT = 10

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        if value > Player.LEVEL_LIMIT:
            value = Player.LEVEL_LIMIT
        self.__level = value


p = Player()
p.level = 100
print(p.level)

class Player:
    pass


class Fighter(Player):
    pass


class Wizard(Player):
    pass


f = Fighter()
print(isinstance(f, Player))
print(isinstance(f, Fighter))
print(isinstance(f, Wizard))

class Player:
    pass


class Fighter(Player):
    pass


class Wizard(Player):
    pass


class MagicKnight(Fighter, Wizard):
    pass


mk = MagicKnight()
print(isinstance(mk, Player))
print(isinstance(mk, Fighter))
print(isinstance(mk, Wizard))
print(isinstance(mk, MagicKnight))

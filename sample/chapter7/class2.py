class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def display(self):
        print('Name :', self.name)
        print('Level:', self.level)


p1 = Player('Daikon', 1)
p1.display()

p2 = Player('Ninjin', 2)
p2.display()

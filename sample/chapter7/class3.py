class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def display(self):
        print('Name :', self.name)
        print('Level:', self.level)

    def level_up(self, number):
        self.level += number


p1 = Player('Daikon', 1)
p1.level_up(2)
p1.display()

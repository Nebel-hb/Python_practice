class Player:
    def display(self):
        print('Name :', self.name)
        print('Level:', self.level)


p1 = Player()
p1.name = 'Daikon'
p1.level = 1
p1.display()

p2 = Player()
p2.name = 'Ninjin'
p2.level = 2
p2.display()

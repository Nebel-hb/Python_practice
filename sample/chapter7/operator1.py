class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def print(self):
        print(self.r, self.g, self.b)


c1 = Color(10, 20, 30)
c1.print()

c2 = Color(40, 50, 60)
c2.print()

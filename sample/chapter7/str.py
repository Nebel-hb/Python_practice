class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __add__(self, other):
        r = self.r + other.r
        g = self.g + other.g
        b = self.b + other.b
        return Color(r, g, b)

    def __str__(self):
        return str(self.r) + ' ' + str(self.g) + ' ' + str(self.b)


c1 = Color(10, 20, 30)
print(c1)

c2 = Color(40, 50, 60)
print(c2)

c3 = c1 + c2
print(c3)

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


def sum(x, y, z):
    return x + y + z


n = sum(1, 2, 3)
print(n)

s = sum('Hello', 'Python', 'World')
print(s)

c = sum(Color(10, 20, 30), Color(40, 50, 60), Color(70, 80, 90))
print(c)

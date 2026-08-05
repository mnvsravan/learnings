class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class line:
    def __init__(self, A, B, C):
        self.a = A
        self.b = B
        self.c = C

    def __str__(self):
        return f"{self.a}x + {self.b}y + {self.c} = 0"

    def line_on_point(self, point):
        return self.a * point.x + self.b * point.y + self.c == 0

    def shortest_distance(self, point):
        return abs(self.a * point.x + self.b * point.y + self.c) / ((self.a ** 2 + self.b ** 2) ** 0.5)


p1 = point(3, 5)
p2 = point(1, 47)

print(p1)
print(p1.distance(p2))

l1 = line(9, 5, 4)
print(l1.line_on_point(p1))
print(l1.shortest_distance(p1))
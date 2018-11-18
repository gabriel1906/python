class Vector:

    def __init__ (self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Vector(self.x + other.x) + (self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x) - (self.y + other.y)


def test_vector_add():
    v1 = Vector(1,3)
    v2 = Vector(4,7)
    result = v1 + v2
    assert result.x == 5
    assert result.y == 10

def test_vector_sub():
    v1 = Vector(1,3)
    v2 = Vector(4,7)
    result = v1 - v2
    assert result.x == -3
    assert result.y == -4
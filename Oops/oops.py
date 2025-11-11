import math


class Counter:
    def __init__(self):
        # Create an instance variable called value. Initialize it to 0
        self.value = 0

    def incr(self):
        # Increments value by 1
        self.value += 1

    def decr(self):
        # Decrements value by 1
        self.value -= 1

    def incrby(self, n):
        # Increments value by n
        if isinstance(n, int):
            self.value += n
        else:
            raise TypeError("n must be an integer")

    def decrby(self, n):
        # Decrements value by n
        if isinstance(n, int):
            self.value -= n
        else:
            raise TypeError("n must be an integer")



class Triangle:
    def __init__(self):
        # Initially an empty list of points
        self.points = []

    def add_point(self, x, y):
        # Adds a point (x, y) to the triangle
        self.points.append((x, y))

    def perimeter(self):
        # Calculates the perimeter of the triangle
        if len(self.points) != 3:
            raise ValueError("A triangle must have exactly 3 points")

        p1, p2, p3 = self.points
        d1 = math.dist(p1, p2)
        d2 = math.dist(p2, p3)
        d3 = math.dist(p3, p1)
        return d1 + d2 + d3

    def is_equal(self, other):
        # Checks whether two triangles have the same list of points
        return self.points == other.points


# Create triangle t1 with points (0,0), (0,3), (4,0)
t1 = Triangle()
t1.add_point(0, 0)
t1.add_point(0, 3)
t1.add_point(4, 0)
print("Perimeter of t1 =", t1.perimeter())

# Create triangle t2 with points (1,2), (2,1), (1,5)
t2 = Triangle()
t2.add_point(1, 2)
t2.add_point(2, 1)
t2.add_point(1, 5)
print("Perimeter of t2 =", t2.perimeter())

# Check whether t1 and t2 are equal
print("t1 == t2 :", t1.is_equal(t2))

# Create triangle t3 with points (1,2), (2,1), (1,5)
t3 = Triangle()
t3.add_point(1, 2)
t3.add_point(2, 1)
t3.add_point(1, 5)

# Perform operations
print("t1 == t3 :", t1.is_equal(t3))
print("t3 == t1 :", t3.is_equal(t1))

# -------------------------------
# Rename is_equal to __eq__
# -------------------------------

class Triangle:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def perimeter(self):
        if len(self.points) != 3:
            raise ValueError("A triangle must have exactly 3 points")

        p1, p2, p3 = self.points
        d1 = math.dist(p1, p2)
        d2 = math.dist(p2, p3)
        d3 = math.dist(p3, p1)
        return d1 + d2 + d3

    def __eq__(self, other):
        return self.points == other.points


# Create t1 and t3 again to test ==
t1 = Triangle()
t1.add_point(0, 0)
t1.add_point(0, 3)
t1.add_point(4, 0)

t3 = Triangle()
t3.add_point(1, 2)
t3.add_point(2, 1)
t3.add_point(1, 5)

# Compare using ==
print("t1 == t3:", t1 == t3)

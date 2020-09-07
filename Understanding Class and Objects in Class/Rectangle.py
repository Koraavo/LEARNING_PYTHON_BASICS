import decimal


def drange(x, y, jump):
    while x < y:
        yield float(x)
        x += decimal.Decimal(jump)


# print(list(drange(0, 10, '0.00001')))
# range = [x/10000 for x in range(0, 10)]
# print(range)

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


class Rectangle:

    def __init__(self, location, width, height):
        self.location = location
        self.width = width
        self.height = height
        self.new_loc = None

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

    def transpose(self):
        self.width, self.height = self.height, self.width

    def contains(self, new_loc):
        return new_loc.x in list(drange(loc.x, self.width, '0.00001')) and new_loc.y in list(
            drange(loc.x, self.height, '0.00001'))

    def diagonal(self):
        d = (self.width ** 2 + self.height ** 2) ** 0.5
        return d

    def collide(self, other):
        pass

    def intersect(self, r2):
        # return not ((x1 + width < x2) or (x2 + width2 < x1) or (y1 + height < y2) or (y2 + height2 < y1))
        # return not (20 < 10 or 30 < 5 or 30 < 5 or 20 < 10)
        # return not ((loc.x + self.width < loc2.x) or (loc2.x + r2.width < loc.x) or (loc.y + self.height < loc2.y) or (
        #             loc2.y + r2.height < loc.y))
        if (loc.x + self.width >= loc2.x) or (loc2.x + r2.width >= loc.x) or (loc2.y + r2.height >= loc.y) or (loc.y + self.height >= loc2.y):
            return "collided"
        else:
            return "not collided"

    def __str__(self):
        return "width=" + str(self.width) + ", height=" + str(self.height) + ", x= " + str(loc.x) + ", y= " + str(loc.y)


loc = Point(0, 0)
r = Rectangle(loc, 10, 5)
loc2 = Point(0, 0)
r2 = Rectangle(loc2, 3, 3)
print(r.contains(Point(3, 4.99999)))
print(r.intersect(r2))


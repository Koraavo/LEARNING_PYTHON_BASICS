# Given three points that fall on the circumference of a circle,
# find the center and radius of the circle.

"""
general form of the equation:
x ** 2 + y ** 2 + 2*g*x + 2*f*y + c = 0


Putting coordinates in eqn of circle, we get:
x12 + y12 + 2gx1 + 2fy1 + c = 0 – (1)
x22 + y22 + 2gx2 + 2fy2 + c = 0 – (2)
x32 + y32 + 2gx3 + 2fy3 + c = 0 – (3)

From (1) we get, 2gx1 = -x12 – y12 – 2fy1 – c – (4)
From (1) we get, c = -x12 – y12 – 2gx1 – 2fy1 – (5)
From (3) we get, 2fy3 = -x32 – y32 – 2gx3 – c – (6)

Subtracting eqn (2) from eqn (1) we get,
2g( x1 – x2 ) = ( x22 -x12 ) + ( y22 – y12 ) + 2f( y2 – y1 ) – (A)

Now putting eqn (5) in (6) we get,
2fy3 = -x32 – y32 – 2gx3 + x12 + y12 + 2gx1 + 2fy1 – (7)

Now putting value of 2g from eqn (A) in (7) we get,
2f = ( ( x12 – x32 )( x1 – x2 ) +( y12 – y32 )( x1 – x2 ) + ( x22 – x12 )( x1 – x3 ) + ( y22 – y12 )( x1 – x3 ) ) / ( y3 – y1 )( x1 – x2 ) – ( y2 – y1 )( x1 – x3 )

Similarly we can obtain the values of 2g :
2g = ( ( x12 – x32 )( y1 – x2 ) +( y12 – y32 )( y1 – y2 ) + ( x22 – x12 )( y1 – y3) + ( y22 – y12 )( y1 – y3 ) ) / ( y3 -y1 )( y1 – y2 ) – ( x2 – x1 )( y1 – y3 )

Putting 2g and 2f in eqn (5) we get the value of c and know we had the equation of circle as x2 + y2 + 2gx + 2fy + c = 0



"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_point(self, point):
        dis = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return dis

    def reflect_x(self):
        return self.x, (-1) * self.y

    def slope_from_origin(self):
        if self.x == 0:
            return None
        else:
            return self.y / self.x

    def slope_between_points(self, point):
        return (point.y - self.y) / (point.x - self.x)

    def get_line_to(self, point):
        m = self.slope_between_points(point)
        b = self.y - (m * self.x)
        return m, b

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def mid_point(self, point):
        return (self.x + point.x) / 2, (self.y+point.y) / 2

    def perpendicular_slope(self, point):
        m = self.slope_between_points(point)
        m1 = (-1) / m
        return m1


    def __str__(self):
        return str(self.x) + "," + str(self.y)


# p = Point(4, 11)
# q = Point(6, 15)
# print(p.get_line_to(q))
point1 = Point(3, 3)
point2 = Point(6, 6)
point3 = Point(10, -4)


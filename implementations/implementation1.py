import turtle
import math

class SierpinskiTriangle:
    def __init__(self, size=640, depth=8):
        self.screen = turtle.Screen()
        self.screen.setup(size, size)
        self.screen.title("Sierpinski Triangle")
        self.screen.bgcolor("white")
        
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        
        self.size = size
        self.depth = depth
        
        self.screen.tracer(0)

    def point_milieu(self, pt1, pt2):
        return ((pt1[0] + pt2[0]) / 2, (pt1[1] + pt2[1]) / 2)

    def draw_triangle(self, a, b, c):
        self.pen.up()
        self.pen.goto(a)
        self.pen.down()
        self.pen.goto(b)
        self.pen.goto(c)
        self.pen.goto(a)

    def sierpinski(self, a, b, c, depth):
        if depth > 0:
            self.draw_triangle(a, b, c)
            
            ab_mid = self.point_milieu(a, b)
            bc_mid = self.point_milieu(b, c)
            ca_mid = self.point_milieu(c, a)
            
            self.sierpinski(a, ab_mid, ca_mid, depth - 1)
            self.sierpinski(ab_mid, b, bc_mid, depth - 1)
            self.sierpinski(ca_mid, bc_mid, c, depth - 1)

    def draw(self):
        margin = 20
        side = self.size - 2 * margin
        height = side * math.sqrt(3) / 2
        
        half_side = side / 2
        x_center = 0
        y_bottom = -height / 2

        pt1 = (x_center - half_side, y_bottom)
        pt2 = (x_center + half_side, y_bottom)
        pt3 = (x_center, y_bottom + height)
        
        self.sierpinski(pt1, pt2, pt3, self.depth)
        
        self.screen.update()
        
        turtle.done()
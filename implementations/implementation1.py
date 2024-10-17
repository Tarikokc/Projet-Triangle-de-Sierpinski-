import turtle
import math

class SierpinskiTriangle:
    def __init__(self, size=640, depth=8):
        # Configuration de l'écran et du stylo pour le dessin
        self.screen = turtle.Screen()
        self.screen.setup(size, size)
        self.screen.title("Sierpinski Triangle")
        self.screen.bgcolor("white")
        
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        
        self.size = size
        self.depth = depth
        
        self.screen.tracer(0)  # Désactive l'animation pour un dessin plus rapide

    def point_milieu(self, pt1, pt2):
        # Calcule le point milieu entre deux points
        return ((pt1[0] + pt2[0]) / 2, (pt1[1] + pt2[1]) / 2)

    def draw_triangle(self, a, b, c):
        # Dessine un triangle en utilisant les coordonnées de ses trois sommets
        self.pen.up()
        self.pen.goto(a)
        self.pen.down()
        self.pen.goto(b)
        self.pen.goto(c)
        self.pen.goto(a)

    def sierpinski(self, a, b, c, depth):
        if depth > 0:
            self.draw_triangle(a, b, c)
            
            # Calcule les points milieux des côtés du triangle
            ab_mid = self.point_milieu(a, b)
            bc_mid = self.point_milieu(b, c)
            ca_mid = self.point_milieu(c, a)
            
            # Appels récursifs pour dessiner les sous-triangles
            self.sierpinski(a, ab_mid, ca_mid, depth - 1)
            self.sierpinski(ab_mid, b, bc_mid, depth - 1)
            self.sierpinski(ca_mid, bc_mid, c, depth - 1)

    def draw(self):
        # Calcule les dimensions et coordonnées du triangle initial
        margin = 20
        side = self.size - 2 * margin
        height = side * math.sqrt(3) / 2
        
        half_side = side / 2
        x_center = 0
        y_bottom = -height / 2

        # Définit les coordonnées des trois sommets du triangle initial
        pt1 = (x_center - half_side, y_bottom)  # Point en bas à gauche
        pt2 = (x_center + half_side, y_bottom)  # Point en bas à droite
        pt3 = (x_center, y_bottom + height)     # Point en haut au milieu
        
        # Lance le processus de dessin récursif
        self.sierpinski(pt1, pt2, pt3, self.depth)
        
        self.screen.update()
        
        turtle.done()  # Termine le dessin et maintient la fenêtre ouverte
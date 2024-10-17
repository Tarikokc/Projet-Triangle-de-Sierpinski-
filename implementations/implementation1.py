import turtle
import math
import time

class SierpinskiTriangle:
    def __init__(self, size=640, depth=8):
        '''
        Initialise la classe SierpinskiTriangle.
        Paramètres:
        - size: taille de l'écran (par défaut 640)
        - depth: profondeur de récursion (par défaut 8)
        '''
        # Configuration de l'écran et du stylo pour le dessin
        self.screen = turtle.Screen()
        self.screen.setup(size, size)
        self.screen.title("Sierpinski Triangle")
        self.screen.bgcolor("white")
        
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        
        self.time_pen = turtle.Turtle()
        self.time_pen.hideturtle()
        self.time_pen.penup()
        
        self.size = size
        self.depth = depth
        
        self.screen.tracer(0)  # Désactive l'animation pour un dessin plus rapide

    def point_milieu(self, pt1, pt2):
        '''
        Calcule le point milieu entre deux points.
        Paramètres:
        - pt1: premier point (tuple x, y)
        - pt2: deuxième point (tuple x, y)
        Retourne: tuple représentant le point milieu
        '''
        return ((pt1[0] + pt2[0]) / 2, (pt1[1] + pt2[1]) / 2)

    def draw_triangle(self, a, b, c):
        '''
        Dessine un triangle en utilisant les coordonnées de ses trois sommets.
        Paramètres:
        - a, b, c: tuples représentant les coordonnées des sommets du triangle
        '''
        self.pen.up()
        self.pen.goto(a)
        self.pen.down()
        self.pen.goto(b)
        self.pen.goto(c)
        self.pen.goto(a)

    def sierpinski(self, a, b, c, depth):
        '''
        Fonction récursive pour dessiner les sous-triangles du triangle de Sierpinski.
        Paramètres:
        - a, b, c: tuples représentant les coordonnées des sommets du triangle
        - depth: profondeur de récursion restante
        '''
        if depth > 0:
            self.draw_triangle(a, b, c)
            
            # Calcule les points milieux des côtés du triangle
            ab_mid = self.point_milieu(a, b)
            bc_mid = self.point_milieu(b, c)
            ca_mid = self.point_milieu(c, a)
            
            self.sierpinski(a, ab_mid, ca_mid, depth - 1)
            self.sierpinski(ab_mid, b, bc_mid, depth - 1)
            self.sierpinski(ca_mid, bc_mid, c, depth - 1)

    def draw(self):
        '''
        Méthode principale pour dessiner le triangle de Sierpinski complet.
        Calcule les dimensions, initialise le dessin et lance le processus récursif.
        '''
        # Calcule les dimensions et coordonnées du triangle initial
        margin = 20
        side = self.size - 2 * margin
        height = side * math.sqrt(3) / 2
        
        half_side = side / 2
        x_center = 0
        y_bottom = -height / 2

        # Définit les coordonnées des trois sommets du triangle initial
        pt1 = (x_center - half_side, y_bottom)  
        pt2 = (x_center + half_side, y_bottom) 
        pt3 = (x_center, y_bottom + height)   
          
        start_time = time.time()

        # Lance le processus de dessin récursif
        self.sierpinski(pt1, pt2, pt3, self.depth)

        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convertir en millisecondes

        self.screen.update()

        # Afficher le temps d'exécution sur l'écran
        self.time_pen.goto(-self.size/2 + 10, self.size/2 - 30)
        self.time_pen.write(f"Temps d'exécution: {execution_time:.2f} ms", font=("Arial", 12, "normal"))
        
        turtle.done()
# Création et exécution du triangle de Sierpinski
sierpinski = SierpinskiTriangle(size=640, depth=6)
sierpinski.draw()
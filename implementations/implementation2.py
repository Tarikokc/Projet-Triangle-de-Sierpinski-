import numpy as np
import pygame
from pygame.locals import *
import time 

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

size = [640,640]
fenetre = pygame.display.set_mode(size)
fenetre.fill(white)

def PointMilieu(Pt1,Pt2):
    return [(Pt1[0]+Pt2[0])/2 , (Pt1[1]+Pt2[1])/2]

def triangle(A,B,C,n):
    if(n>0):
        pygame.draw.polygon(fenetre,black,[A,B,C],1)
        triangle(A,PointMilieu(A,B),PointMilieu(A,C),n-1)
        triangle(PointMilieu(A,B),B,PointMilieu(B,C),n-1)
        triangle(PointMilieu(A,C),PointMilieu(B,C),C,n-1)
            
Pt1=[10,630]
Pt2=[630,630]
Pt3=[320,93]

start_time = time.time()

triangle(Pt1,Pt2,Pt3,8)

end_time = time.time()

# Calculer la durée en millisecondes
execution_time = (end_time - start_time) * 1000
print(f"Durée d'exécution: {execution_time:.2f} ms")

pygame.display.flip()

continuer=True
while continuer:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            continuer=False
            

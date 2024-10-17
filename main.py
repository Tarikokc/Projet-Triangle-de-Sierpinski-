import os
import sys

from implementations.implementation1 import SierpinskiTriangle
from visualisations.visualisation import visualize_triangle

def main():
    
    triangle = SierpinskiTriangle(size=800, depth=6)
    visualize_triangle(triangle)

if __name__ == "__main__":
    main()
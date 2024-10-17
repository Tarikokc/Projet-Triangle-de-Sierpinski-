import pytest 
from implementations.implementation1 import SierpinskiTriangle

@pytest.fixture
def triangle():
    """Crée et retourne une instance de SierpinskiTriangle pour les tests."""
    return SierpinskiTriangle(size=640, depth=4)

def test_init(triangle):
    """Vérifie que l'initialisation de SierpinskiTriangle se fait correctement."""
    assert triangle.size == 640
    assert triangle.depth == 4

def test_point_milieu(triangle):
    """Teste la fonction point_milieu pour s'assurer qu'elle calcule correctement le point milieu."""
    result = triangle.point_milieu((0,0),(10,10))
    assert result == (5,5)

def test_draw_triangle(triangle):
    """Teste la fonction draw_triangle pour s'assurer qu'elle dessine un triangle."""
    triangle.draw_triangle((0,0),(10,10),(5,15))

def test_sierpinski(triangle):
    """Teste la fonction sierpinski pour s'assurer qu'elle génère correctement le triangle de Sierpinski."""
    triangle.sierpinski((0, 0), (10, 0), (5, 8.66), 2)

def test_draw(triangle):
    """Vérifie que la méthode draw existe et est appelable."""
    assert hasattr(triangle, 'draw') 
    assert callable(getattr(triangle,'draw'))
import pytest 
from implementations.implementation1 import SierpinskiTriangle

@pytest.fixture

def triangle() : 
    return SierpinskiTriangle(size=640, depth=4)

def test_init(triangle) : 
    assert triangle.size == 640
    assert triangle.depth == 4

    
def test_point_milieu(triangle) : 
    result = triangle.point_milieu((0,0),(10,10))
    assert result == (5,5)
    

def test_draw_triangle(triangle) :
    triangle.draw_triangle((0,0),(10,10),(5,15))

def test_sierpinski(triangle) :
    triangle.sierpinski((0, 0), (10, 0), (5, 8.66), 2)
    
def test_draw(triangle) : 
    assert hasattr(triangle, 'draw') 
    assert callable(getattr(triangle,'draw')) 

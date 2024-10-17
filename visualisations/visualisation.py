import turtle

def visualize_triangle(sierpinski_triangle):
    screen = sierpinski_triangle.screen
    pen = sierpinski_triangle.pen

    margin = 20
    side = sierpinski_triangle.size - 2 * margin
    height = side * (3 ** 0.5) / 2
    
    half_side = side / 2
    x_center = 0
    y_bottom = -height / 2

    pt1 = (x_center - half_side, y_bottom)
    pt2 = (x_center + half_side, y_bottom)
    pt3 = (x_center, y_bottom + height)

    pen.clear()
    
    sierpinski_triangle.sierpinski(pt1, pt2, pt3, sierpinski_triangle.depth)

    screen.update()

    turtle.done()

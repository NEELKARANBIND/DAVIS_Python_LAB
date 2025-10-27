# create a module for calculating area of 2dfigures(triangle,circle,square,rectangle)
def area_triangle(base, height):
    #Calculate the area of a triangle.
    return 0.5 * base * height


def area_circle(radius):
    #Calculate the area of a circle.
    pi = 3.14159
    return pi * radius * radius


def area_square(side):
    #Calculate the area of a square.
    return side * side


def area_rectangle(length, width):
    #Calculate the area of a rectangle.
    return length * width


# Optional test section
if __name__ == "__main__":
    print("Area of triangle (base=10, height=5):", area_triangle(10, 5))
    print("Area of circle (radius=7):", area_circle(7))
    print("Area of square (side=4):", area_square(4))
    print("Area of rectangle (length=8, width=3):", area_rectangle(8, 3))

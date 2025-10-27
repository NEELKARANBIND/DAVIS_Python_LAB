# A program to calculate the area and perimeter of a triangle using functions

def calculate_area(base, height):
    return 0.5 * base * height

def calculate_perimeter(side1, side2, side3):
    return side1 + side2 + side3

# Input from the user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Calculate area and perimeter
area = calculate_area(base, height)
perimeter = calculate_perimeter(side1, side2, side3)

# Print the results
print("Area of the triangle:", area)
print("Perimeter of the triangle:", perimeter)


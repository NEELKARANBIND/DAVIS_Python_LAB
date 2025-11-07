#a program to input any three sides of triangle and check  they form a triangle or not ,if they form triangle  then specify the type of triangle
 # identify the type of triangle
 
 #input: Three sides of triangle
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))  
side3 = float(input("Enter length of side 3: "))
 
 #function to check if sides from a triangle
 def is_triangle(a, b, c):
     return a + b > c and a + c > b and b + c > a
 
    #function to determine the type of triangle
 def triangle_type(a, b, c):
     if a == b == c:
         return "Equilateral"
     elif a == b or b == c or a == c:
         return "Isosceles"
     else:
         return "Scalene"

#main logic
 if is_triangle(side1, side2, side3):
     print("The sides from a triangle.")
     print("Type of triangle:", triangle_type(side1, side2, side3))
 else:
     print("The sides do not form a triangle.")
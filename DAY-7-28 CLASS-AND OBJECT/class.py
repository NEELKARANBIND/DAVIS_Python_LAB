#syntax for defining a class in python
''' class className:
#member variables
variable = value
#methods
def methodName(self, parameters):
#working

#Syntax for creating an object of a class
objectName = className()
'''
#Defining a class for rectangle
class Rectangle:
    #member variables
    length = 0
    breadth = 0

    #method for input of data
    def inputData(self):
        self.length = int(input("Enter length of rectangle: "))
        self.breadth = int(input("Enter breadth of rectangle: "))
        
        #method for display data
    def displayData(self):
        print("Length of rectangle:", self.length)
        print("Breadth of rectangle:", self.breadth)
        
        #method to calculate perimeter
    def calculatePerimeter(self):    
        perimeter = 2 * (self.length + self.breadth)
        print("Perimeter of rectangle:", perimeter)
        #method to calculate area of a rectangle
        def calculateArea(self):
            area = self.length * self.breadth
            print("Area of rectangle:", area)
        
        #main program
#object creation
rect = Rectangle()
rect.inputData()
rect.displayData()
rect.calculatePerimeter()
rect.calculateArea()

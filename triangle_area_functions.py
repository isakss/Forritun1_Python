#This program takes three vertices of a triangle as an input, uses them to find the euclidean distance between each point
#and then uses herons formula to calculate the area of the triangle in question. The calculations and the vertice insertion 
#will be done by use of functions

import math

#We start by defining the input function to get the vertex

def get_vertex():
    x = float(input("Enter the value of x: "))
    y = float(input("Enter the value of y: "))

    return x,y

#Next we want to define a function that can implement a triangle from three seperate calls to get_vertex

def get_triangle():
    print("First vertex")
    x1, y1 = get_vertex()
    print("Second vertex")
    x2, y2 = get_vertex()
    print("Third vertex")
    x3, y3 = get_vertex()

    return x1, y1, x2, y2, x3, y3

#Next we define a function that can calculate the length of the triangles sides, we use the euclidean distance formula to do so

def side_length(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

#And finally we create a function that calculates the area of a triangle by making use of the side_length function and Herons formula

def calculate_area(x1,y1,x2,y2,x3,y3):
    a = side_length(x1,y1,x2,y2)
    b = side_length(x2,y2,x3,y3)
    c = side_length(x3,y3,x1,y1)
    s = (1/2) * (a + b + c)

    return round(math.sqrt(s * (s - a) * (s - b) * (s - c)),2) 

#And now we create the main part of our program, which gets the appropriate values of vertex and passes them into the calculation function

x1,y1,x2,y2,x3,y3 = get_triangle()
triangle_area = calculate_area(x1,y1,x2,y2,x3,y3)

print("The area of the triangle in question is: {}".format(triangle_area))



import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
import random
import math

# Parameters
delta = 3.0
qInit = [50.0,50.0]
domain = [100.0,100.0]
k = 10
# Parameters 

class point:
    
    # This is the list of points that self has
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.children = []

    # For testing
    def printChildren(self):
        for i in range(len(self.children) ):
            print(str(self.children[i].x) + " " + str(self.children[i].y)  )


class circle:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

points = []

# Insert description here 
def generateRandomPoint():
    global domain

    randomX = random.random() * domain[0]
    randomY = random.random() * domain[1]
   
    return point(randomX, randomY)


# Calculate distance between two points
def calculateDistance(point1, point2):
    
      
    distance = (point1.x - point2.x)**2 + (point1.y - point2.y)**2
    distance = math.sqrt(distance)

    return distance


# Insert description here
def findNearestPoint(newPoint):
    
    global points
    minPoint = points[0]
    minDistance = 9999999999999999
    # Traverse the list of points and calculate the min
    for i in range(len(points) ):
        
        distance =  calculateDistance(points[i], newPoint) 
        if ( minDistance >=  distance ):
            minDistance = distance 
            minPoint = points[i]
     
    # Add the new point to the list
    # minPoint.children.append(newPoint)
    # points.append(newPoint)
    
    return minPoint


# Insert description here
def calculateDistanceToCenter(point1, point2, circle):
    
    vectorX = float(point2.x - point1.x)
    vectorY = float(point2.y - point1.y)

    lengthOfVector = math.sqrt(vectorX**2 + vectorY**2)
    
    AD = circle.x - point1.x
    
    ED = abs(circle.y - point1.y)
    
    return ED

# Given the newPoint and the closest point, generate the 
# point that we will add to the graph
def findNewConfiguration(closestPoint, newPoint):
    
    global delta
    global points

    vectorX = float(newPoint.x - closestPoint.x)
    vectorY = float(newPoint.y - closestPoint.y)
    
    lengthOfVector = math.sqrt(vectorX**2 + vectorY**2)


    # Scale the length of the vector
    # plt.plot(50, 55)
    # FIX ME - divide by step variable
    vectorX = (float(vectorX) / float(lengthOfVector) ) * delta
    vectorY = (float(vectorY) / float(lengthOfVector) ) * delta

    # Calculate the new point
    finalPoint = point(closestPoint.x + vectorX, closestPoint.y + vectorY)
    # finalPoint = point(newPoint.x + vectorX, newPoint.y + vectorY)

    #print(" ") 
    #print(str(closestPoint.x) + ", " + str(closestPoint.y) ) 
    #print(str(finalPoint.x) + ", " + str(finalPoint.y) )
    #print(" ")


    # Add to list of children
    closestPoint.children.append(finalPoint)
    # Describe
    points.append(finalPoint)

    return finalPoint 

# Insert description of this method here 
def addNewPoint():
    
    # This is the list of all the points
    global points

    newPoint = generateRandomPoint()
    # print(str(newPoint.x) + "," + str(newPoint.y) )
    minPoint = findNearestPoint(newPoint)
    findNewConfiguration(minPoint, newPoint) 


# This takes a list of points and plots 
# all the points and edges 
def plotAllPoints():
   
    global points
    
    # Plot the lines
    for i in range(0, len(points) ):
        for j in range( len(points[i].children ) ):
            plt.plot( [points[i].x, points[i].children[j].x], [points[i].y,  points[i].children[j].y] 
                    , linewidth = 0.3) 

    # Plot the points
    for i in range(0, len(points) ):
        plt.plot(  [points[i].x], [points[i].y],  marker='o', markersize=1, color="red")
       
    
    #plt.xlim(0, 100)
    #plt.ylim(0, 100)
    plt.show()


# Add the initial point
points.append(point(qInit[0], qInit[1]) )

point1 = point(2,2)
point2 = point(3,2)
circle1 = circle(0, 0, 1)

print( calculateDistanceToCenter(point1, point2, circle1) )


for i in range(0, 500):
    addNewPoint()

plotAllPoints()


plt.show()

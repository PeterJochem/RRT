import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.collections import LineCollection
import random
import math
from itertools import product, combinations


# Parameters
delta = 1.0
qInit = [50.0, 50.0, 50.0]
domain = [100.0, 100.0, 100.0]
k = 10
# Parameters 
points = []
spheres = []
goalPath = []

class point:
    
    # This is the list of points that self has
    def __init__(self, x, y, z, parent = None):
        self.x = x
        self.y = y
	self.z = z
        self.children = []
        self.parent = parent

    # For testing
    def printChildren(self):
        for i in range(len(self.children) ):
            print(str(self.children[i].x) + " " + str(self.children[i].y) + " " + str(self.children[i].z)  )


# Insert description here
class sphere:

    def __init__(self, x, y, z, radius):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius

# Insert description here 
def generateRandomPoint():
    global domain

    randomX = random.random() * domain[0]
    randomY = random.random() * domain[1]
    randomZ = random.random() * domain[2]	
 
    return point(randomX, randomY, randomZ)


# Calculate distance between two points
def calculateDistance(point1, point2):
    
      
    distance = (point1.x - point2.x)**2 + (point1.y - point2.y)**2 + (point1.z - point2.z)**2
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


# Given the newPoint and the closest point, generate the 
# point that we will add to the graph
def findNewConfiguration(closestPoint, newPoint):
    
    global delta
    global points

    vectorX = float(newPoint.x - closestPoint.x)
    vectorY = float(newPoint.y - closestPoint.y)
    vectorZ = float(newPoint.z - closestPoint.z)   	
 
    lengthOfVector = math.sqrt(vectorX**2 + vectorY**2 + vectorZ**2)

    # Scale the length of the vector
    # FIX ME - divide by step variable
    vectorX = (float(vectorX) / float(lengthOfVector) ) * delta
    vectorY = (float(vectorY) / float(lengthOfVector) ) * delta
    vectorZ = (float(vectorZ) / float(lengthOfVector) ) * delta	

    # Calculate the new point
    finalPoint = point(closestPoint.x + vectorX, closestPoint.y + vectorY, closestPoint.z + vectorZ)

    # Add to list of children
    closestPoint.children.append(finalPoint)
    # Describe
    points.append(finalPoint)
    
    # Set the parent field of the new point
    finalPoint.parent = closestPoint

    return finalPoint 


# This method calculates the minimum distance between the center of the sphere 
# and the vector defined by the two points newPoint and minPoint
# It returns the minimum distance
def calculateMinDistance(newPoint, minPoint, currentSphere):

    numerator = (currentSphere.x - newPoint.x) * (minPoint.x - newPoint.x)
    numerator = numerator + (currentSphere.y - newPoint.y) * (minPoint.y - newPoint.y) 
    numberator = float( numerator + (currentSphere.z - newPoint.z) * (minPoint.z - newPoint.z) )
    
    denominator = float(math.sqrt( ( (minPoint.x - newPoint.x)**2) + ( (minPoint.y - newPoint.y)**2) + ( (minPoint.z - newPoint.z)**2) ) )
    denominator = float(denominator**2)
    
    u = float(numerator / denominator)

    x = newPoint.x + u * (minPoint.x - newPoint.x)
    y = newPoint.y + u * (minPoint.y - newPoint.y)
    z = newPoint.z + u * (minPoint.z - newPoint.z)
    
    distance = math.sqrt(  (currentSphere.x - x)**2  + (currentSphere.y - y)**2 +  (currentSphere.z - z)**2  )

    return distance

# This method calculates if the vector defined by newPoint and minPoint 
# intersects any of the spheres in the system
# Returns True if the vector intersects any of the spheres in the system
# Returns False otherwise 
def isConflict(newPoint, minPoint):
    
    global spheres

    for i in range(0, len(spheres) ):
        if ( calculateMinDistance(newPoint, minPoint, spheres[i] ) <= spheres[i].radius ):
            return True

    return False
    

# This method adds a new point to the global list of 
# all the points in the system. It generates a point randomnly
# then finds the point closest already in the system to that point
# It then adds the point delta away in that direction to the globa list
def addNewPoint():
    
    # This is the list of all the points
    global points
    
    # Init here so scope is available below do-while
    minPoint = 0
    newPoint = 0

    # Do while in Python
    while(True):
        newPoint = generateRandomPoint()
        minPoint = findNearestPoint(newPoint)
        if ( isConflict(newPoint, minPoint) == False):
            break
       
    # Set the parent field so we can trace backwards to it
    finalPoint = findNewConfiguration(minPoint, newPoint) 

    # Check if the new point is < 5% of the domain length from the goal point
    if ( calculateDistance(finalPoint, goalPoint) < ( 0.05 * domain[0] ) ):
   
        # Is there a clear path to the goal? IE the line hits no obstacles
        if ( isConflict(newPoint, goalPoint ) == False ):
            goalPoint.parent = finalPoint
            return True

    return False


# This method is more for testing and needs chnages
# Randonmly gnerate a point to draw a sphere around
def insertSphere():
    
    global spheres
    global domain
    
    # FIX - NO spheres within sphere!?????
    
    randomX = random.random() * domain[0]
    randomY = random.random() * domain[1]
    randomZ = random.random() * domain[2]
    
    randomRadius = random.random() * domain[0] / 10

    # For testing
    spheres.append(sphere(randomX, randomY, randomZ, randomRadius) )


# This method will calculate the distance from a vector (ie line) to
# the center of the circle
def distanceToCenter(point1, point2, circle):
    
    vectorX = point2.x - point1.x
    vectorY = point2.y - point1.y
    
    vectorLength = math.sqrt(vectorX**2 + vectorY**2)
    
    distance = vectorLength * math.cos( )


# insert description here 
def traceGoalPath():
    
    global goalPath
    global goalPoint
    
    currentPoint = goalPoint

    while( currentPoint is not None ):
        goalPath.append(currentPoint)
        currentPoint = currentPoint.parent
        

# Insert description here 
def plotGoalPath():
    
    global goalPath
    global goalPoint

    traceGoalPath()
    
    fig = plt.figure()
    ax = plt.axes(projection = '3d')

    print("After tracing the goal path, its length is " + str(len(goalPath) ) ) 
    
    for i in range(1, len(goalPath) ):
        # print( str(goalPath[i].x) + ", " + str( goalPath[i].y )  )
        ax.plot3D( [ goalPath[i].x, goalPath[i - 1].x], [goalPath[i].y, goalPath[i - 1].y],  [goalPath[i].z, goalPath[i - 1].z] )

    
    # Plot the circle
    # From StackOverFlow
    for i in range(len(spheres) ):
        # Make data
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)

        radius = spheres[i].radius

        x = ( radius * ( np.outer(np.cos(u), np.sin(v) ) ) )
        y = ( radius * ( np.outer(np.sin(u), np.sin(v) ) ) )
        z = ( radius * ( np.outer(np.ones(np.size(u)), np.cos(v) ) ) )

        # Plot the surface
        ax.plot_surface(x + spheres[i].x, y + spheres[i].y, z + spheres[i].z, color='b')

    ax.set(xlim=(0, domain[0]),  ylim=( 0, domain[1] ), zlim = ( 0, domain[2] )   )
    plt.show()




# This takes a list of points and plots 
# all the points and edges 
def plotAllPoints():
   
    global points
    global spheres
   
    fig = plt.figure()
    ax = plt.axes(projection = '3d')

    xData = []
    yData = []
    zData = []
    
    # Add all the points to the lists
    for i in range(0, len(points) ):
        
        xData.append(  points[i].x  )
        yData.append(  points[i].y  )
        zData.append(  points[i].z  )

    ax.scatter3D(xData, yData, zData, c = zData, cmap = 'Greens')

    # Plot the points
    for i in range(0, len(points) ):
        for j in range( len(points[i].children ) ): 
            ax.plot3D( [points[i].x, points[i].children[j].x], [points[i].y, points[i].children[j].y], [points[i].z, points[i].children[j].z] )  
   
        
    # Plot the circle 
    # From StackOverFlow 
    for i in range(len(spheres) ):
        # Make data
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)

        radius = spheres[i].radius
    
        x = ( radius * ( np.outer(np.cos(u), np.sin(v) ) ) )
        y = ( radius * ( np.outer(np.sin(u), np.sin(v) ) ) )
        z = ( radius * ( np.outer(np.ones(np.size(u)), np.cos(v) ) ) ) 

        # Plot the surface
        ax.plot_surface(x + spheres[i].x, y + spheres[i].y, z + spheres[i].z, color='b')
    
    ax.set(xlim=(0, domain[0]),  ylim=( 0, domain[1] ), zlim = ( 0, domain[2] )   )
    plt.show()


# Add the initial point
points.append(point(qInit[0], qInit[1], qInit[2])  )


# FIX ME
# FIX - Make sure the obstacles do not cover the goal point!!!!!
# FIX ME
# FIX ME 
goalPoint = point(20,20,40)

for i in range(0, 4):
    insertSphere()


reachedGoal = False

upperRange = 400000
for i in range(0, upperRange):
    if (reachedGoal == False):
        if ( addNewPoint() == True):
            reachedGoal = True
            plotGoalPath()
            plt.show()
            break
 
plotAllPoints()


    



plt.show()

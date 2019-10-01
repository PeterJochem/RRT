
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection


# Parameters
delta = 1
qInit = [50,50]
domain = [100,100]
k = 10
# Parameters 



# Some example data to display
#x = np.linspace(0, 2 * np.pi, 400)
#y = np.sin(x ** 2)


# This lets us put more plots onto the same "Plot"
# It subdivivdes one screen into many diffrent plots
#fig, axs = plt.subplots(4)
#fig.suptitle('Vertically stacked subplots')
#axs[0].plot(x, y)
#axs[1].plot(x, -y)
#axs[2].plot(-y, x)
#axs[3].plot(-x,-y)


# LinePlot is a list of lines
# LinePlot = ListOfLines
# Each Line = [x,y],[x,y]

#point1 = np.array([1,2])
#point2 = np.array([3,4])
#point3 = np.array([5,6])
#point4 = np.array([7,8])

#line1 = np.array([])
#np.append(line1, point1)
#np.append(line1, point2)

#line2 = np.array([])
#np.append(line2, point3)
#np.append(line2, point4)

#lineSegs = np.array([])
#np.append(lineSegs,line1)
#np.append(lineSegs, line2)

#line_segments = LineCollection(lineSegs, linewidths=(0.5, 1, 1.5, 2) )
#fig, ax = plt.subplots()
#ax.set_xlim(0, 10)
#ax.set_ylim(0, 10)

#ax.add_collection(line_segments)



fig, ax = plt.subplots()
x = [[1,2], [3,4]]
y = [[5,6], [7,9]]
plt.plot(x)
plt.plot(y)

# lineN = [ point, point ]
# plt.plot(lineN)









plt.show()

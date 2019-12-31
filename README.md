# How To Run My Code
To run the RRT for searching throuh 3-D spaces, simply run ```python3 RRT_3D.py```.To run the 2-D implementation, simply run ```python3 RRT_2D.py```

# Description
The Rapidly Exploring Random Tree is a path planning algorithm. It effectively searches through high dimensional spaces for viable paths from one state to another. It easily lends itself to spaces with constraints and arbitrary obstacles. It is commonly used in robotics. Steven LaValle developed it and the original paper can be found at http://msl.cs.uiuc.edu/~lavalle/papers/Lav98c.pdf. My implementation searches through 2-D and 3-D spaces with circular and spherical obstacles. It returns a viable path from the inital position to the desired postion while avoiding the obstacles.

# Results
The blue spheres are obstacles for the algorithm to avoid. The stochastic, multi colored points are those on the tree.

This is a plotting of all the points on the RRT.

![This is the result of the 3-D RRT]( https://github.com/PeterJochem/RRT/blob/master/all_Points.png "All the Points on the 3-D RRT")

This is an RRT plotted with just the points on the goal path.

![This is the result of the 3-D RRT]( https://github.com/PeterJochem/RRT/blob/master/goalPath.png "Path Found by RRT")

This is the 2-D plotting of all the points on the tree.
![This is the result of the 2-D RRT]( https://github.com/PeterJochem/RRT/blob/master/2D.png  "2-D RRT")




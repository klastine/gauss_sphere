# gauss_sphere
A programmatic solution to the Gauss Circle problem

The Gauss Circle problem is a mathematical problem to find a closed formula for the number of "lattice points" within a given circle. 
Lattice points are any point where both x and y are integer values. In other words, where you'd see crossing lines on graph paper.
While this program does not provide a closed formula, it does count the number of lattice points in a very time-efficent manner. 
Not only does it calculate lattice points for circles, but also spheres, hyperspheres, and any other circle-based object in any number of dimensions.
By recognizing and accounting for the pattern of symmetry within these objects, the computational expenditure only increases linearly with the number of dimensions.
Unfortunately, it is probably mathematically impossible to replicate this for the radius parameter, so runtime increases exponentially with radius. 
Even still, it is fairly interesting that a 10 dimensional calculation would take only twice as long as a 5 dimensional one.

To check it out, just download the gauss_sphere.py file and use the gss function which has paramaters dimensions and radius, in that order.
For example, one might try "gss(4,10)" to calculate the exact number of lattice points within a 4-dimensional hypersphere of radius 10.
On my machine, this takes about 0.003 seconds to compute to 49689. 

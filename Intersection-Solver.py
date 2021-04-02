import math
import collections
from typing import Literal

#def function to return 
def calculateIntersection(quadratic_eq,linear_eq):
    b=quadratic_eq.B -linear_eq.slope
    c=quadratic_eq.C - linear_eq.yInt
    
    discriminant = b**2 - (4 * quadratic_eq.A * c)

    if discriminant > 0:
        print("There are 2 points of Intersection")
        x1=(-b + math.sqrt(discriminant)) / (2.0 * quadratic_eq.A)
        x2=(-b - math.sqrt(discriminant)) / (2.0 * quadratic_eq.A)

        return discriminant, [(x1, (linear_eq.slope * x1) + linear_eq.yInt), (x2, (linear_eq.slope * x2) + linear_eq.yInt)]

    elif discriminant == 0.0:
        print("There is only one point of intersection")
        x1= -b / (2.0*quadratic_eq.A)
        return discriminant, [x1, (linear_eq.slope * x1) + linear_eq.yInt]
    else:
        print("No points of intersection")
        return discriminant, []

linear_eq = collections.namedtuple('linear_eq', 'slope yInt')
quadratic_eq = collections.namedtuple('quadratic_eq', 'A B C')

#Input variable values here
quadratic_eq = quadratic_eq( A=3, B=4, C=-7)
linear_eq = linear_eq(slope = 16 , yInt= 19 )
(discriminant, points) = calculateIntersection(quadratic_eq, linear_eq)

if (len(points) > 0):
    print("Intersection: {}".format(points))
else:
  print("No intersection: {}".format(discriminant))
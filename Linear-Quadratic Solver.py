import math
import collections


def calculateIntersection(p, l):
  b = p.B - l.slope
  c = p.C - l.yInt

  discriminant = b**2 - (4 * p.A * c)

  if discriminant > 0.0:
    # 2 points of intersection
    x1 = (-b + math.sqrt(discriminant)) / (2.0 * p.A)
    x2 = (-b - math.sqrt(discriminant)) / (2.0 * p.A)

    return discriminant, [(x1, l.slope * x1 + l.yInt), (x2, l.slope * x2 + l.yInt)]

  elif discriminant == 0.0:
    # 1 point of intersection
    x1 = -b / (2.0 * p.A)

    return discriminant, [(x1, slope * x1 + l.yInt)]
  else:
    # no points of intersection
    return discriminant, []


Line = collections.namedtuple('Line', 'slope yInt')
Poly = collections.namedtuple('Poly', 'A B C')

p = Poly(A=-3.09363812e-04, B=1.52138019e+03, C=-1.87044961e+09)
print(p)

l = Line(slope=1.06446434e-03, yInt=-2.61660911e+03)
print(l)

(discriminant, points) = calculateIntersection(p, l)

if (len(points) > 0):
  print("Intersection: {}".format(points))
else:
  print("No intersection: {}".format(discriminant))
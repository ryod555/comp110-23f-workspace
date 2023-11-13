"""Testing point methods."""

from lessons.cq07.point import Point

my_point: Point = Point(10, 15)

my_point.scale_by(2)
print(my_point.x)

print(my_point.scale(2).x)
'''
Write a Python program to convert degree to radian.
Input degree: 15
Output radian: 0.261904

Write a Python program to calculate the area of a trapezoid.
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5

Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625

Write a Python program to calculate the area of a parallelogram.
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0
'''
import math
import numpy as np
#1

def degrees_to_radians(degrees):
  radians = degrees * math.pi / 180
  return radians

print('%.6f' % degrees_to_radians(15.0))
#2
def trapezoid():
    #Area = (base1 + base2) * height / 2
    base1 = int(input('input base1: '))
    base2 = int(input('input base2: '))
    height = int(input('input height: '))
    return (base1 + base2) * height/2
print(trapezoid())
#3
def regular_polygon():
    sides = int(input('input number of sides: '))
    length = int(input('input length of each side: '))
    cot = 1 / np.tan(math.pi/sides)
    area = sides/4 * length**2 * cot
    area = round(area)
    return area
print(regular_polygon())
#4
def paralel():
   b = int(input('input base: '))
   h = int(input('input height: '))
   return b * h
print(paralel())
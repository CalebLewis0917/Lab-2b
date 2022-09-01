# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Caleb Lewis
# Section:      521
# Assignment:   Lab 2b
# Date:         10 Sep 2021
#

from math import *

# t is time in seconds
t1 = 12
t2 = 85
t01 = 30
t02 = 60

# x, y, and z are positions on a 3D graph
x1 = 2
x2 = 25

y1 = 3
y2 = -5

z1 = 7
z2 = 11

# Linear interpolation formula used for each variable at t = t01
t0 = t01
x0 = ((x2-x1)/(t2-t1))*(t0-t1)+x1
y0 = ((y2-y1)/(t2-t1))*(t0-t1)+y1
z0 = ((z2-z1)/(t2-t1))*(t0-t1)+z1

print("At time",t0,"seconds:")
print("x0 =",x0,"m")
print("y0 =",y0,"m")
print("z0 =",z0,"m")
print("----------------------")

# Linear interpolation formula used for each variable at t = t01+(t02-t01)/4
t0 = t01+(t02-t01)/4
x0 = ((x2-x1)/(t2-t1))*(t0-t1)+x1
y0 = ((y2-y1)/(t2-t1))*(t0-t1)+y1
z0 = ((z2-z1)/(t2-t1))*(t0-t1)+z1

print("At time",t0,"seconds:")
print("x0 =",x0,"m")
print("y0 =",y0,"m")
print("z0 =",z0,"m")
print("----------------------")

# Linear interpolation formula used for each variable at t = t01+((t02-t01)/4)*2
t0 = t01+((t02-t01)/4)*2
x0 = ((x2-x1)/(t2-t1))*(t0-t1)+x1
y0 = ((y2-y1)/(t2-t1))*(t0-t1)+y1
z0 = ((z2-z1)/(t2-t1))*(t0-t1)+z1

print("At time",t0,"seconds:")
print("x0 =",x0,"m")
print("y0 =",y0,"m")
print("z0 =",z0,"m")
print("----------------------")

# Linear interpolation formula used for each variable at t = t01+((t02-t01)/4)*3
t0 = t01+((t02-t01)/4)*3
x0 = ((x2-x1)/(t2-t1))*(t0-t1)+x1
y0 = ((y2-y1)/(t2-t1))*(t0-t1)+y1
z0 = ((z2-z1)/(t2-t1))*(t0-t1)+z1

print("At time",t0,"seconds:")
print("x0 =",x0,"m")
print("y0 =",y0,"m")
print("z0 =",z0,"m")
print("----------------------")

# Linear interpolation formula used for each variable at t = t02
t0 = t02
x0 = ((x2-x1)/(t2-t1))*(t0-t1)+x1
y0 = ((y2-y1)/(t2-t1))*(t0-t1)+y1
z0 = ((z2-z1)/(t2-t1))*(t0-t1)+z1

print("At time",t0,"seconds:")
print("x0 =",x0,"m")
print("y0 =",y0,"m")
print("z0 =",z0,"m")

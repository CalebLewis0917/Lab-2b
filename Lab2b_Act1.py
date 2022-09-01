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

# Force Calculation
mass = 2 # kg
accel = 5 # m/s^2
force = mass*accel
print ("Force is", force, "N")

# Wavelength Calculation
distance = .025 # nm
angle = .436332313 # radians
print ("Wavelength is", (2*distance)*sin(angle), "nm")

# Mass Calculation
initialM = 3 # grams
time = 5 # days
half_life = 3.8 # days
print ("Radon-222 left is", initialM*(2**(-time/half_life)), "g")

# kPa Calculation
moles = 5 # moles
volume = .15 # m^3
temp = 425 # Kelvin
gConstant = .008314 # m^3kPa/K*mol
print ("Pressure is", moles*gConstant*temp/volume, "kPa")


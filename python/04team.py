print ('Welcome to the velocity calculator. Please enter the following: ')
print ('')
#---------------------------------------------------------------------------------------------
Mass = float(input('Mass (in kg): '))
Gravity = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
Time = float(input('Time (in seconds): '))
Density = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
Cross = float(input('Cross sectional area (in m^2): '))
Drag = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))
r = float(input('What is the radius of the bowlling ball?: '))
#---------------------------------------------------------------------------------------------
import math
exp = math.exp
sqrt = math.sqrt
pi = math.pi
c = 1 / 2 * Density * Cross * Drag
Cross_Section_Area = pi * r ** 2
csa = 1 / 2 * Density * Cross_Section_Area * Drag

velocity = sqrt((Mass * Gravity) / c) * (1 - exp((-sqrt(Mass * Gravity * c)/Mass) * Time))
velocity2 = sqrt((Mass * Gravity) / csa) * (1 - exp((-sqrt(Mass * Gravity * csa)/Mass) * Time))
#---------------------------------------------------------------------------------------------
print (f'The inner value of c is: {c:.3f}')
print (f'The velocity after {Time} seconds is: {velocity:.3f} m/s')
print (f'The velocity of a Bowlling ball after {Time} seconds is: {velocity2:.3f} m/s')
from math import pi, sin, cos, sqrt
from numpy import arcsin

def main():
    #describe user what is goin' on
    print("Hi, this programm will compute the measures of your triangle, if you have exactly: side - angel - side.")
    print("Two sides and the angle between them.")
    print("(Note that the triangle is determined by these three values.)")
    
    #ask user for importrant informations
    firstSide = input("How long is the first side? (in mm)  ")
    angle = input("How big is your angle? (in °)  ")
    secondSide = input ("How long is the second side? (also in mm)  ")

    # compute
    b = float(firstSide)
    c = float(secondSide)
    alpha = float(angle) / 180 * pi
    a = sqrt((b * sin(alpha))**2 + (c - b * cos(alpha))**2)
    # use sinus theorem
    sinusBeta = b / a * sin(alpha)
    if (a**2 + c**2 >= b**2):
        # angle beta is sharp
        beta = arcsin(sinusBeta)
    else:
        beta = pi - arcsin(sinusBeta)
    gamma = pi - alpha - beta

    
    #finally output
    print(" ")
    print("The description of the triangle:")
    something = "something"
    print("a = {:.0f} mm".format(a))
    print("b = {:.0f} mm".format(b))
    print("c = {:.0f} mm".format(c))
    print("Angle alpha = {:.1f} °".format(alpha / pi * 180))
    print("Angle beta  = {:.1f} °".format(beta  / pi * 180))
    print("Angle gamma = {:.1f} °".format(gamma / pi * 180))
    
main()

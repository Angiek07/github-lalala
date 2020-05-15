import turtle #don't forget to import also turtle.Screen()
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
    if (a**2 + c**2 <= b**2):
        # angle beta is sharp
        beta = arcsin(sinusBeta)
    else:
        beta = pi - arcsin(sinusBeta)
    gamma = pi - alpha - beta

    #turtle drawing

    #finally output
    print(" ")
    print("The description of the triangle:")
    something = "something"
    print(format("""Last side lenght is " + something )
    print("Angle between your first side and our 'new side' is " + something + "°")
    print("Angle between your second side and our 'new side' is " + something + "°")
    print(" ")
    print("You can also look at this basic graph... :)")
main()

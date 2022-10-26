# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.

import math

xc1 = 4
yc1 = 4.25

xc2 = 53
yc2 = -5.35

# Calculate the distance between the two circle
def distance_between_two_circles(x1, y1, x2, y2):
    distance = math.sqrt((x1-x2)**2 + (y1 - y2)**2)
    return distance

print('Distance: ', distance_between_two_circles(xc1, yc1, xc2, yc2))

# *** somewhere else in your program ***
xa = -36
ya = 97

xb = .34
yb = .91

# calcualte the length of vector AB vector which is a vector between A and B points.

def calculate_vector_length(xa, ya, xb, yb):
    length = math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))
    return length

print('Length:', calculate_vector_length(xa, ya, xb, yb))

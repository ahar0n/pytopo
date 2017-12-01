# python lib to surveying compute

from math import pi
from math import sqrt
from math import atan, cos, sin

def foresight(fs0, angle):
    ''' 
    returns the foresight azimuth (rad), from azimuth i-1 (fs0)
    and angle at station poitn to foresight station
    '''
    alpha = fs0 + angle
    if alpha < pi:
        return alpha + pi
    elif alpha >= 3 * pi:
        return alpha - 2 * pi
    else:
        return alpha - pi

def grad2rad(x):
    ''' returns x (grad) in radians '''
    return x * pi / 200

def rad2grad(x):
    ''' returns x (rad) in gradians '''
    return x * 200 / pi

def distance(i, j):
    ''' returns distance between 2 points '''
    return sqrt((j[0] - i[0])**2 + (j[1] - i[1])**2)

def azimuth(i, j):
    ''' 
    returns the foresight azimuth (rad) from i to j.
    i and j are vectors (x, y).
    '''
    dx = j[0] - i[0]
    dy = j[1] - i[1]
    if dx == 0:
        if dy > 0:
            return 0
        else:
            return pi
    elif dy == 0:
        if dx > 0:
            return pi/2
        else:
            return 3 / 2 * pi
    else:
        a = atan(dx/dy)
        if dy < 0:
            return a + pi
        elif dx < 0:
            return a + 2 * pi
        else:
            return a
        
def angle(b, i ,f):
    ''' 
    returns the angle (rad) clockwise bif.
    b, i and f are vector (x, y).
    '''
    azDiff = azimuth(i, f) - azimuth(i, b)
    if azDiff < 0:
        return azDiff + 2 * pi
    else:
        return azDiff

def dNorth(azimuth, distance):
    '''
    returns delta north from foresight azimuth (rad) and
    distance.
    '''
    return distance * cos(azimuth)

def dEast(azimuth, distance):
    '''
    returns delta east from foresight azimuth (rad) and
    distance.
    '''
    return distance * sin(azimuth)
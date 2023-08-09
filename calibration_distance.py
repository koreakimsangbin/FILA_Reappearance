from math import pi

def calculate_distance(c, f0, CSIeff, sigma, n):

    distance = (1 / (4 * pi)) * (((c / f0 * abs(CSIeff)) * (c / f0 * abs(CSIeff))) * sigma) ** (1 / n)
    return distance

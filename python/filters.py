import math

"""
Consumes pointes (distance, ...)
Yields same values until value greater than max is found
"""
def max_distance(max, points):
    for point in points:
        if point[0] > max:
            break
        yield point

"""
Consumes points (distance, easting, northing)
Yields points (distance, easting, northing, height)
"""
def add_height(dtm, points):
    for distance, easting, northing in points:
        yield (distance, easting, northing, dtm.get_height(easting, northing))


"""
Consumes points (distance, easting, northing, height)
Yields points (distance, easting, northing, height, elevation)
"""
def add_elevation(local_height, points):
    for distance, easting, northing, height in points:
        yield (distance, easting, northing, height, math.atan((height - local_height) / distance))



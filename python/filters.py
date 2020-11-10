#
# Horizon Generator - Python
#
# Copyright (c) 2020 Nick Banyard
#
import math

def max_distance(max, points):
    """
    Consumes points (distance, ...)
    Yields same values until value greater than max is found
    """
    for point in points:
        if point[0] > max:
            break
        yield point

def add_height(dtm, points):
    """
    Consumes points (distance, easting, northing)
    Yields points (distance, easting, northing, height)
    """
    for distance, easting, northing in points:
        yield (distance, easting, northing, dtm.get_height(easting, northing))


def add_elevation(local_height, points):
    """
    Consumes points (distance, easting, northing, height)
    Yields points (distance, easting, northing, height, elevation)
    """
    for distance, easting, northing, height in points:
        yield (distance, easting, northing, height, math.atan((height - local_height) / distance))

def remove_hidden(points):
    """
    Consumes (..., elavation)
    Yields same values, removing any points hidden by closer points
    """
    point = next(points)
    max_elevation = point[-1]
    yield point
    for point in points:
        if point[-1] > max_elevation:
            yield point
            max_elevation = point[-1]


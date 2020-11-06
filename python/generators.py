import math
import itertools

def generate_by_northings(startEastings, startNorthings, bearing, step):
    dir = math.cos(bearing) < 0 and -1 or 1
    tan = math.tan(bearing) * dir
    cos = abs(math.cos(bearing))

    for north_distance in itertools.count(step, step):
        yield((
            int(north_distance / cos),
            int(startEastings + north_distance * tan),
            startNorthings + north_distance * dir
        ))

def generate_by_eastings(startEastings, startNorthings, bearing, step):
    dir = math.sin(bearing) < 0 and -1 or 1
    tan = math.tan(bearing) * dir
    sin = abs(math.sin(bearing))

    for east_distance in itertools.count(step, step):
        yield((
            int(east_distance / sin),
            startEastings + east_distance * dir,
            int(startNorthings + east_distance / tan)
        ))

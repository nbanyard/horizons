#
# Horizon Generator - Python
#
# Copyright (c) 2020 Nick Banyard
#
import math
import itertools

def generate_by_northings(startEastings, startNorthings, bearing, step):
    """
    Walk along bearing, stepping on northings that separate posts in TDM

    Each step yields (direct_distance, easting, northing)
    """
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
    """
    Walk along bearing, stepping on eastings that separate posts in TDM

    Each step yields (direct_distance, easting, northing)
    """
    dir = math.sin(bearing) < 0 and -1 or 1
    tan = math.tan(bearing) * dir
    sin = abs(math.sin(bearing))

    for east_distance in itertools.count(step, step):
        yield((
            int(east_distance / sin),
            startEastings + east_distance * dir,
            int(startNorthings + east_distance / tan)
        ))

def generate_on_bearing(startEastings, startNorthings, bearing, step):
    """
    Walk along bearing, stepping as close as possible to the centre of each post in TDM

    Steps are not evenly spaced, but aim to make best use of TDM

    Each step yields (direct_distance, easting, northing)
    """
    by_northings = generate_by_northings(startEastings, startNorthings, bearing, step)
    by_eastings = generate_by_eastings(startEastings, startNorthings, bearing, step)

    last_step = None
    next_northings = next(by_northings)
    next_eastings = next(by_eastings)

    while next_northings or next_eastings:
        if next_northings[0] < next_eastings[0]:
            this_step = next_northings
            next_northings = next(by_northings)
        else:
            this_step = next_eastings
            next_eastings = next(by_eastings)
        if last_step:
            yield (
                int((last_step[0] + this_step[0]) / 2),
                int((last_step[1] + this_step[1]) / 2),
                int((last_step[2] + this_step[2]) / 2)
            )
        last_step = this_step

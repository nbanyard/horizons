#
# Horizon Generator - Python
#
# Copyright (c) 2020 Nick Banyard
#

def distance_colour(distance, max_distance, near_colour, far_colour):
    proportion = distance / max_distance
    return (
        (far_colour[0] - near_colour[0]) * proportion + near_colour[0],
        (far_colour[1] - near_colour[1]) * proportion + near_colour[1],
        (far_colour[2] - near_colour[2]) * proportion + near_colour[2]
    )


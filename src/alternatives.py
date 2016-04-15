"""Module to determine the percentage increase in alternative paths."""

from __future__ import division
import operator

import networkx as nx


def _path_length(city, path):
    """Return the total length of a path."""
    sum_length = 0
    for i in range(len(path) - 1):
        sum_length += city[path[i]][path[i+1]]['length']

    return sum_length


def get_parameter(city, route):
    """Main function to return the value of Parameter 2

    This function is based on the percantage increase in traffic of alternate
    pathways of the commute direction of a route.
    """
    all_alternates = list()
    for path in nx.all_simple_paths(city, route[1], route[0]):
        if len(path) == 2:
            continue
        elif len(path) == 3:
            all_alternates.append(path)
        elif len(path) > 3:
            break
    alternates_dict = dict()
    for pathway in all_alternates:
        alternates_dict[tuple(pathway)] = _path_length(city, pathway)

    # Take only two alternate pathways
    try:
        path_a = sorted(alternates_dict.items(),
                        key=operator.itemgetter(1))[0][0]
        path_a_length = sorted(alternates_dict.items(),
                               key=operator.itemgetter(1))[0][1]
        path_aa = city[path_a[0]][path_a[1]]
        path_ab = city[path_a[1]][path_a[2]]
    except IndexError:
        raise IndexError("No alternatives available for this route.")
    try:
        path_b = sorted(alternates_dict.items(),
                        key=operator.itemgetter(1))[1][0]
        path_b_length = sorted(alternates_dict.items(),
                               key=operator.itemgetter(1))[1][1]
        path_ba = city[path_b[0]][path_b[1]]
        path_bb = city[path_b[1]][path_b[2]]
    except IndexError:
        # That just means there is just path_a
        pass

    del all_alternates, alternates_dict
    # path_a and path_b are the alternate pathways for the route.

    route_b = city[route[1]][route[0]]

    num = path_aa['threshold']*path_aa['length']*path_aa['lanes'] + \
          path_ab['threshold']*path_ab['length']*path_ab['lanes']
    denom = path_aa['length'] + path_ab['length']
    total_threshold = num/denom

    old_cars = 0  # Old number of cars flowing in alterate pathways
    old_cars += path_aa['car_density']*path_aa['length']
    old_cars += path_ab['car_density']*path_ab['length']

    if path_b:
        num = path_ba['threshold']*path_ba['length'] + \
              path_bb['threshold']*path_bb['length']
        denom = path_ba['length'] + path_bb['length']
        total_threshold += num/denom

        old_cars += path_ba['car_density']*path_ba['length']
        old_cars += path_bb['car_density']*path_bb['length']

    delta_cars = route_b['car_density']*route_b['length']  # Cars to be diverted

    new_cars = old_cars + delta_cars

    new_car_density = new_cars / (path_a_length + path_b_length)

    if total_threshold*path_aa['lanes'] <= new_car_density:
        return False
    else:
        old_car_density = old_cars / (path_a_length + path_b_length)
        delta_car_density = new_car_density - old_car_density
        return delta_car_density / old_car_density

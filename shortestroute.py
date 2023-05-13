    # We are given an array of 2D coordinates representing points in space.
    # Goal is to find the shortest route that visits all the points in the array and returns to the starting point
    # The algorithm starts at the first coordinate, selects the nearest unvisited coordinate, and continues until all coordinates are visited.

import math

def calculate_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

def find_shortest_route(coordinates):
    route = []
    current_coordinate = coordinates[0]
    coordinates = coordinates[1:]

    route.append(current_coordinate)

    while coordinates:
        min_distance = float('inf')
        for coord in coordinates:
            distance = calculate_distance(current_coordinate, coord)
            if distance < min_distance:
                min_distance = distance
                nearest_coord = coord
        
        route.append(nearest_coord)
        current_coordinate = nearest_coord
        coordinates.remove(nearest_coord)

    route.append(coordinates[-1])

    return route

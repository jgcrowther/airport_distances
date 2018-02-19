from geopy.distance import vincenty


def find_nearest_airport(coords, airports):
    """
    Takes list of float coords and dictionary of airports. Uses geopy and the vincenty algorithm to
    determine the distance between points. Returns name of airport and lowest distance found after 
    checking all airports in the dict.
    """
    nearest_airport = None
    nearest_airport_dist = None
    for airport in airports:
        airport_coords = (airports[airport].get("lat"), airports[airport].get("lon"))
        dist = vincenty(airport_coords, coords).miles
        if nearest_airport_dist == None:
            nearest_airport_dist = dist
            nearest_airport = airport
        elif dist < nearest_airport_dist:
            nearest_airport_dist = dist
            nearest_airport = airport
    return nearest_airport, nearest_airport_dist

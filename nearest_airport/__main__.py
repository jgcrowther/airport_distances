from .generate_airports import generate
from .user_input import user_input
from .find_nearest_airport import find_nearest_airport


airports = generate()
coords = user_input()
nearest_airport, nearest_airport_dist = find_nearest_airport(coords, airports)

if __name__ == "__main__":
    print("The nearest airport to '%s' is %s: %s, which is %0.2f miles away" 
        % (
            ", ".join([str(c) for c in coords]), 
            airports[nearest_airport].get("ICAO"), 
            nearest_airport.title(), 
            nearest_airport_dist))

import csv


def generate():
    """
    Assumes airports.csv file is located in root folder. Converts this file to a dictionary, 
    where the keys are the airport names, and the values are another dictionary of the remaining
    columns in the csv. Returns dictionary.
    """
    airports_table = csv.reader(open('airports.csv', mode='r'))
    next(airports_table)
    airports = {}

    for row in airports_table:
        airports.update({row[0]: {
            "ICAO": row[1],
            "lat": row[2],
            "lon": row[3],
        }})
    
    return airports
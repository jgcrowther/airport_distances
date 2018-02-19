import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import unittest
from nearest_airport import find_nearest_airport, generate_airports
from airport_distances.find_nearest_airport import dist_between_two_points


class TestFindNearestAirport(unittest.TestCase):
    airports = generate_airports.generate()
    airport_keys = list(airports.keys())

    def test_result_against_list(self):
        """
        Tests each airports lat/lon coordinates against itself, expects to see the airport name and a distance of 0.0
        """
        case = [[float(self.airports[n].get("lat")), float(self.airports[n].get("lon"))] for n in self.airport_keys]
        for i, coords in enumerate(case):
            self.assertEqual(find_nearest_airport.find_nearest_airport(coords, self.airports), 
                (self.airport_keys[i], 0.0))

    def test_manual_coords(self):
        """
        Test some manual coordinates found an measured on google
        Accuracy of test measurment is not 100%, which is why the distance
        is checked between two values
        """
        coords = [50.837240, -0.268848]
        result_airport, result_dist = find_nearest_airport.find_nearest_airport(coords, self.airports)
        self.assertEqual(result_airport, "SHOREHAM")
        self.assertTrue(0.5 < round(result_dist, 1) < 1.5)

        coords = [51.479820, -0.612742]
        result_airport, result_dist = find_nearest_airport.find_nearest_airport(coords, self.airports)
        self.assertEqual(result_airport, "HEATHROW")
        self.assertTrue(6.2 < round(result_dist, 1) < 7.3)


class TestAirportDistances(unittest.TestCase):
    def test_known_cases_as_float_list(self):
        """
        Test known distance between two lat/lon coords when coords are a list of floats
        """
        airport_1 = [52.342611,0.772939]
        airport_2 = [52.628611,-3.153333]
        self.assertEqual(round(dist_between_two_points(airport_1, airport_2), 2), 145.02)

    def test_known_cases_as_string(self):
        """
        Test known distance between two lat/lon coords when coords are comma separated string
        """
        airport_1 = '52.342611, 0.772939'
        airport_2 = '52.628611, -3.153333'
        self.assertEqual(round(dist_between_two_points(airport_1, airport_2), 2), 145.02)

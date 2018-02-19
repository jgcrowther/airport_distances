import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import unittest
from nearest_airport import user_input


class TestFindNearestAirport(unittest.TestCase):
    def test_working_normally(self):
        """
        Test that a correct input returns a list of floats
        """
        origional_input = __builtins__.input
        __builtins__.input = lambda _: '52, 52'
        self.assertEqual(user_input.user_input(), [52, 52])
        __builtins__.input = origional_input
    
    def test_check_value(self):
        """
        Tests that the check_value function return true for strings that are numbers and
        False for strings that are not numbers
        """
        self.assertTrue(user_input.check_value("52"))
        self.assertFalse(user_input.check_value("A"))
    
    def test_process_coords(self):
        """
        Test the process_coords function takes a list of string numbers and converts it to a list of floats
        """
        self.assertEquals(user_input.process_coords(["52", "52"]), [52.0, 52.0])

unittest.main()

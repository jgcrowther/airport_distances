# Lat/Lon Coordinates Nearest Airport

## Prerequisites

Developed and tested with Python 3.6.1

Requirments found in requiremtns.txt


## Running the module

### For User input lat/lon:
Navigate terminal to project directory and run 'python nearest_airport'. Input your coordinates and receive nearest airport and distance.

### For Plotly/Dash airport to airport distances:
Navigate terminal to project directory and run 'python -m airport_distances'. Navigate to the IP address given in the terminal using an internet browser.


## Running the tests

Navigate terminal to project directory and run 'python -m tests' for the main tests
To test the user input run 'python tests/user_input_test.py'

### Tests explanation

find_nearest_airport_test.py tests the function that accepts input coordinates from user, finds the nearest airport from the provided csv file, and returns the airport's name and distance.

e.g.
input: 52.342611, 0.772939
returns: 'HONINGTON', 0.0

user_input_test.py tests if a correct input works, and returns a coordinates list. 

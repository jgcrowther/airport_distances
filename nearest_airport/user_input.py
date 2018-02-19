def check_value(value):
    """
    Checks if the string can be converted to a float. 
    Had to write this as str.isdigit() doesn't work with negatives
    """
    try:
        float(value)
        return True
    except:
        return False

def process_coords(coords):
    """
    Accepts a list of strings and converts all values to floats
    """
    return [float(n) for n in coords]

def user_input():
    """
    Gets input from terminal, checks that it is comma seperated and the input values are numbers
    """
    while True:
        user_input = input("Please enter comma seperated coordinates: ")
        user_input = user_input.replace(" ", "")
        
        try:
            coords = user_input.split(",")
            if len(coords) != 2:
                print("Please enter a decimal latitude and longitude e.g: '52.342611, 0.772939'")
                continue
            elif not check_value(coords[0]) or not check_value(coords[1]):
                print("Please enter a decimal latitude and longitude as a floating point number e.g: '52.342611, 0.772939'")
                continue
            return process_coords(coords)
        except:
            print("Please enter a decimal latitude and longitude with comma seperation. E.g: '52.342611, 0.772939'")
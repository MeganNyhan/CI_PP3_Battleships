"""
Legend:
1. "." = water or empty space.
2."O" - part of ship.
3."X" = part of ship that was hit with a bullet.
4."#" = Water that was shot with a bullet. This is a miss.
"""

# Global variable for grid
GRID = [[]]
# Global variable for grid size
GRID_SIZE = 10
# Global variable for number of ships you have to place
NUM_OF_SHIPS = 8
# Global variable of bullets you have left
BULLETS_LEFT = 50
# Global variable for game over
GAME_OVER = False
# Global variable for number of ships you have sunk
NUM_OF_SHIPS_SUNK = 0
# Global variable for ship positions on grid
SHIP_POSITIONS = [[]]
# Global variable for alphabet on side of grids
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """
        This is the validate_grid_and_place_ship function.
        It will check the row or column to see if you can place your ship down on the grid.
        It will return a True or False statement.
    """
    global GRID
    global SHIP_POSITIONS

    pass


def try_to_place_ship_on_grid(row, col, direction, length):
    """
        This is the try_to_place_ship_on_grid function.
        It is based on direction that will call the helper method to try and place a ship on the grid.
        This will return the validate_grid_and_place_ship function which will confirm if its True or False.
    """
    global GRID_SIZE

    pass

    return validate_grid_and_place_ship(0, 0, 0, 0)


def create_grid():
    """ 
        This is the create grid function.
        This will create a 15x15 grid and randomly place down ships of different sizes in different directions.
        This will have no return but will use the try_to_place_ship_on_grid.
    """
    global GRID
    global GRID_SIZE
    global NUM_OF_SHIPS
    global SHIP_POSITIONS      

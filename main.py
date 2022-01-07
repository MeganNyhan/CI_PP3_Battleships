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
#Global variable for number of ships you have sunk
NUM_OF_SHIPS_SUNK = 0
#Global variable for ship positions on grid
SHIP_POSITIONS = [[]]
#Global variable for alphabet on side of grids
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



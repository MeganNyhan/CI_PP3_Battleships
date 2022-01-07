"""
Legend:
1. "." = water or empty space.
2."O" - part of ship.
3."X" = part of ship that was hit with a bullet.
4."#" = Water that was shot with a bullet. This is a miss.
"""

# Variables use in the game:
# Global variables used for Grid:
grid = [[]]
# Global variable for grid size:
grid_size = 10
# Global variable for number of ships to use:
num_of_ships = 8
# Global variable for bullets left to use:
bullets_left = 50
# Global variable for game over:
game_over = False
# Global variable for number of ships sunk
num_of_ships_sunk = 0
# Global variable for ship positions:
ship_positions = [[]]
# Global variable for alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
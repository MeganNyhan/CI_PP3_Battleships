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
        It will check the row or column to see if you can place your ship down 
        on the grid.
        It will return a True or False statement.
    """
    global GRID
    global SHIP_POSITIONS

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if GRID[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        SHIP_POSITIONS.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                GRID[r][c] = "O"
    return all_valid
 

def try_to_place_ship_on_grid(row, col, direction, length):
    """
        This is the try_to_place_ship_on_grid function.
        It is based on direction that will call the helper method to try and 
        place a ship on the grid.
        This will return the validate_grid_and_place_ship function which will 
        confirm if its True or False.
    """
    global GRID_SIZE

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= GRID_SIZE:
            return False
        end_col = col + length
    
    elif direction == "down":
        if row + length >= GRID_SIZE:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)


def create_grid():
    """ 
        This is the create grid function.
        This will create a 10x10 grid and randomly place down ships of different
        sizes in different directions.
        This will have no return but will use the try_to_place_ship_on_grid.
    """
    global GRID
    global GRID_SIZE
    global NUM_OF_SHIPS
    global SHIP_POSITIONS      

    random.seed(time.time())

    rows, cols = (GRID_SIZE, GRID_SIZE)

    GRID = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        GRID.append(row)

    NUM_OF_SHIPS_PLACED = 0

    SHIP_POSITIONS = []

    while NUM_OF_SHIPS_PLACED != NUM_OF_SHIPS:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            NUM_OF_SHIPS_PLACED += 1


def print_grid():
    """
        This is the print grid function.
        This will print the grid with rows A - J and 0 - 9 making it 10x10.
        This has a no return.
    """ 
    global GRID  
    global ALPHABET
    
    debug_mode = True

    ALPHABET = alphabet[0: len(GRID) + 1]

    for row in range (len(GRID)):
        print(ALPHABET(row), end=") ")
        for col in range(len(GRID[row])):
            if GRID[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(GRID[row][col], end=" ")
        print("")

    print(" ", end=" ")
    for i in range(len(GRID[0])):
        print(str(i), end=" ")
    print("")

def accept_valid_bullet_placement():
    """ 
        This is the bullet placement function.
        This will get a valid row and column to place the bullet you shoot.
        This has a return for row, column - both being integers.
    """
    global ALPHABET
    global GRID

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
        placement = input("Enter row (A-J) and column (0-9) such as A3: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column such as A3")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        row = ALPHABET.find(row)
        if not (-1 < row < GRID_SIZE):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        if GRID[row][col] == "#" or GRID[row][col] == "X":
            print("You have already shot a bullet here, pick somewhere else")
            continue
        if GRID[row][col] == "." or GRID[row][col] == "O":
            is_valid_placement = True

    return row, col


def check_for_ship_sunk(row, col):
    """ 
        This is the check_for_ship_sunk function.
        This will check if all the parts of the ship have been shot and if so
        the ship is sunk.
        It has a return value of True or False.
    """
    global SHIP_POSITIONS
    global GRID

    for position in SHIP_POSITIONS:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            # Ship found, now check if its all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if GRID[r][c] != "X":
                        return False
    return True


def shoot_bullet():
    """
        This is the function for shooting bullets.
        It will update the grid and ships based on where the bullet was aimed 
        and shot.
        It has no return but will use accept_valid_bullet_position function.
    """
    global GRID
    global NUM_OF_SHIPS_SUNK
    global BULLETS_LEFT

    row, col = accept_valid_bullet_placement()

    pass


def check_for_game_over():
    """ 
        This is the check for game over function.
        This will check to see if all ships have sunk if so the game is over.
        It will also check for the amount of bullets we have remaining, if it 
        goes to 0 the game will end.
        Has no return.
    """
    global NUM_OF_SHIPS_SUNK
    global NUM_OF_SHIPS
    global BULLETS_LEFT
    global GAME_OVER

    pass


def main():
    """ 
        This function will run the game loop.
        It has no return, but will use create_grid, print_grid, shoot_bullet, 
        and check_for_game_over.
    """
    global GAME_OVER

    pass


if __name__ == '__main__':
    """ 
        This will only be called when the program is run from the terminal or 
        an IDE like PyCharms
    """
    main()
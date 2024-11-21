from numpy import array

class Config:
    DEFAULT_WIN_WIDTH = 1280
    DEFAULT_WIN_HEIGHT = 720
    FPS = 60

    MOVEMENT_SPEED = array([4, 4]) # a <-> d, w <-> s directional movement speed
    MOVEMENT_RESRICTIONS = [0.2, 0.2] # percentage of [width, height] the player cannot physically move to.#

    DEFAULT_CHARACTER = 1
    NUMBER_OF_CHARACTERS = 3 # number of character imgs in "assets\player\"
    GAME_PLAYING_CAPTION = "goblin shooter"

    PRINT_TIMEOUT = 2000 # time to display print statements on-screen (ms)

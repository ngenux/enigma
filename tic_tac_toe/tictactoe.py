# Import necessary modules and classes
from view import IntroDisplay, GameDisplay
from model import Players, Game
from controller import PlayerManager, GameManager, GameOptionManager
from utils import console
from rich.text import Text

if __name__ == "__main__":
    # Start the game loop
    while True:
        round = 1

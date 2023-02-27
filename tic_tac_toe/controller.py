import random, time
from rich.text import Text
from rich.prompt import Prompt
from utils import console, GameTools
from model import Players, Game
from view import GameDisplay
import subprocess, sys


class PlayerManager:
    """
    Manages the players of the Tic Tac Toe game.

    Args:
        players_instance (Players): The instance of the Players class.

    Attributes:
        players (Players): The instance of the Players class.

    Methods:
        get_player_names: Prompts the user to enter the names of the two players.
        get_player_colors: Generates colors for the two players.
        greet_players: Greets the two players and displays their names and colors.
        shuffle_players: Shuffles the order of the players and their colors.
        get_mark_colors: Generates colors for the X and O marks.
        get_player_marks: Prompts the user to choose their mark (X or O) and displays it.
        initialize_player_scores: Initializes the scores of the two players to 0.
    """

    def __init__(self, players_instance: Players) -> None:
        self.players = players_instance

    def get_player_names(self) -> None:
        """Prompts the user to enter the names of the two players."""
        pass

    def get_player_colors(self) -> None:
        """Generates colors for the two players."""
        pass

    def greet_players(self) -> None:
        """Greets the two players and displays their names and colors."""
        pass

    def shuffle_players(self) -> None:
        """Shuffles the order of the players and their colors."""
        pass

    def get_mark_colors(self) -> None:
        """Generates colors for the X and O marks."""
        pass

    def get_player_marks(self) -> None:
        """Prompts the user to choose their mark (X or O) and displays it."""
        pass

    def initialize_player_scores(self) -> None:
        """Initializes the scores of the two players to 0."""
        pass


class GameManager:
    """
    Manages the game flow and tracks scores.

    Args:
        game_display_instance (GameDisplay): An instance of the `GameDisplay` class.

    Attributes:
        game_display (GameDisplay): An instance of the `GameDisplay` class.

    Methods:
        game_loop(round): Manages the game flow for a single round.
        game_over(): Prompts the user to play another round or quit the game.
    """

    def __init__(self, game_display_instance: GameDisplay) -> None:
        """
        Initializes the GameManager instance.

        Args:
            game_display_instance (GameDisplay): An instance of the `GameDisplay` class.
        """
        self.game_display = game_display_instance

    def game_loop(self, round) -> None:
        """
        Manages the game flow for a single round.

        Displays the current board, lets each player make a move in turn, checks for a win or tie, and returns the
        scores for the round.

        Args:
            round (int): The number of the current round.

        Returns:
            list: A list of the current scores for each player.
        """
        pass

    def game_over(self) -> bool:
        """
        Prompts the user to play another round or quit the game.

        Returns:
            bool: `True` if the user wants to play another round, `False` otherwise.
        """
        pass


class GameOptionManager:
    """
    A class to manage game options such as starting, restarting, and exiting the game.

    Attributes:
    -----------
    game_instance: Game
        An instance of the Game class.
    player_instance: Players
        An instance of the Players class.
    player_manager_instance: PlayerManager
        An instance of the PlayerManager class.

    Methods:
    --------
    start_game() -> List[str]:
        Prompts the user to start the game and shuffles the players if they agree.
        Returns a list of player names in a random order.
    exit_game() -> bool:
        Prompts the user if they want to exit the game and quits if they agree.
        Returns True if the user agrees to exit, False otherwise.
    restart_game() -> None:
        Clears the console screen, displays a message and waits for 3 seconds before restarting the game.
    """

    def __init__(
        self,
        game_instance: Game,
        player_instance: Players,
        player_manager_instance: PlayerManager,
    ) -> None:
        """
        Initializes a new instance of the GameOptionManager class.

        Parameters:
        -----------
        game_instance: Game
            An instance of the Game class.
        player_instance: Players
            An instance of the Players class.
        player_manager_instance: PlayerManager
            An instance of the PlayerManager class.
        """
        self.game = game_instance
        self.players = player_instance
        self.player_manager = player_manager_instance

    def start_game(self) -> None:
        """
        Prompts the user to start the game and shuffles the players if they agree.

        Returns:
        --------
        List[str]:
            A list of player names in a random order.
        """
        pass

    def exit_game(self) -> bool:
        """
        Prompts the user if they want to exit the game and quits if they agree.

        Returns:
        --------
        bool:
            True if the user agrees to exit, False otherwise.
        """
        pass

    def restart_game(self) -> None:
        """
        Clears the console screen, displays a message and waits for 3 seconds before restarting the game.
        """
        pass

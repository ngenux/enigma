from typing import List
from utils import console
from rich.text import Text
from rich.prompt import Prompt


class Players:
    def __init__(self, num_players: int, player_marks: List[str]):
        """
        Represents the players in a game.

        Args:
            num_players (int): The number of players in the game.
            player_marks (List[str]): A list of strings containing the unique marks assigned to each player.

        Raises:
            ValueError: If the number of players does not match the length of the player marks list.
        """
        if len(player_marks) != num_players:
            raise ValueError("Number of players and marks don't match.")
        self.num_players = num_players
        self.player_names = []
        self.player_colors = []
        self.player_marks = player_marks
        self.mark_colors = []
        self.player_scores = []


class Game:
    def __init__(self):
        """
        Represents a game of Tic Tac Toe.

        Initializes an empty 3x3 board with each cell containing a list of a blank space and the color green.
        """
        self.board = [[[" ", "green"] for _ in range(3)] for _ in range(3)]

    def player_move(
        self, player_name: str, player_color: str, player_mark: str, mark_color: str
    ) -> List[List[str]]:
        """
        Handles a player's move in the game. Displays the current player's name and mark color, prompts the player
        to enter a row and column for their move, checks if the chosen position is available, updates the board
        if it is, and returns the updated board.

        Args:
            player_name (str): The name of the player who is making the move.
            player_color (str): The color of the player's name (e.g. "red", "blue").
            player_mark (str): The symbol that the player is using for their moves (e.g. "X", "O").
            mark_color (str): The color of the player's symbol (e.g. "green", "yellow").

        Returns:
            List of lists representing the updated game board after the player's move.

        Raises:
            None.

        Example:
            board = [[[' ', 'green'], [' ', 'green'], [' ', 'green']], [[' ', 'green'], [' ', 'green'], [' ', 'green']], [[' ', 'green'], [' ', 'green'], [' ', 'green']]]
            player_move("John", "blue", "X", "red")
            # prompts user to enter row and column numbers
            # if user enters 2 and 3
            # returns board = [[[' ', 'green'], [' ', 'green'], [' ', 'green']], [[' ', 'green'], [' ', 'green'], ['X', 'red']], [[' ', 'green'], [' ', 'green'], [' ', 'green']]]
        """

        # Prints the current player's name and their mark color in a bold and blinking
        console.print(
            Text(f"{player_name}'S MOVE -", style=f"bold {player_color} blink"),
            Text(player_mark, style=f"bold {mark_color} blink"),
        )
        while True:
            # Asks the player to enter the row number, with choices of 1, 2, or 3
            row = (
                int(
                    Prompt.ask(
                        Text("Enter row number", style="green"), choices=["1", "2", "3"]
                    )
                )
                - 1
            )
            # Asks the player to enter the column number, with choices of 1, 2, or 3
            col = (
                int(
                    Prompt.ask(
                        Text("Enter column number", style="green"),
                        choices=["1", "2", "3"],
                    )
                )
                - 1
            )
            # Check if the position is already occupied
            if self.board[row][col][0] != " ":
                console.print(
                    "That position is already occupied. Please choose a different position.",
                    style="red",
                )
                continue
            # update the board with the entered position
            self.board[row][col] = [player_mark, mark_color]
            return self.board

    def check_win(self, player_mark: str) -> bool:
        """
        Checks if the specified player has won the game.

        Args:
            player_mark (str): The mark assigned to the player being checked.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        # check rows
        for row in range(3):
            if all(self.board[row][col][0] == player_mark for col in range(3)):
                return True
        # check columns
        for col in range(3):
            if all(self.board[row][col][0] == player_mark for row in range(3)):
                return True
        # check diagonals
        if all(self.board[i][i][0] == player_mark for i in range(3)):
            return True
        if all(self.board[i][2 - i][0] == player_mark for i in range(3)):
            return True
        return False

    def check_tie(self) -> bool:
        """
        Checks if the game has ended in a tie.

        Returns:
            bool: True if the game has ended in a tie, False otherwise.
        """
        for row in range(3):
            for col in range(3):
                if self.board[row][col][0] == " ":
                    return False
        return True

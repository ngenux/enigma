from typing import List


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

    def check_win(self, player_mark):
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

    def check_tie(self):
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

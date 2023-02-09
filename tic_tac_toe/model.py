import time, random
from typing import List, Tuple
from rich.text import Text
from rich.prompt import Prompt
from utils import GameTools, console


class Players:
    def __init__(self, num_players: int, player_marks: List[str]):
        if len(player_marks) != num_players:
            raise ValueError("Number of players and marks don't match.")
        self.num_players = num_players
        self.player_names = []
        self.player_marks = player_marks
        self.mark_colors = []
        self.player_colors = []
        self.player_scores = []


class Game:
    def __init__(self):
        self.board = [" " for x in range(9)]

    def check_tie(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col][0] == " ":
                    return False
        return True

    def check_win(self, player_mark):
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

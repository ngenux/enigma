import random, time
from rich.text import Text
from rich.prompt import Prompt
from utils import console, GameTools
from model import Players, Game
from view import GameDisplay
import subprocess, sys


class PlayerManager:
    def __init__(self, players_instance: Players):
        self.players = players_instance

    def get_player_names(self):
        pass

    def get_player_colors(self):
        pass

    def greet_players(self):
        pass

    def shuffle_players(self):
        pass

    def get_mark_colors(self):
        pass

    def get_player_marks(self):
        pass

    def initialize_player_scores(self):
        pass


class GameManager:
    def __init__(self, game_display_instance: GameDisplay):
        self.game_display = game_display_instance

    def game_loop(self, round):
        pass

    def game_over(self):
        pass


class GameOptionManager:
    def __init__(
        self,
        game_instance: Game,
        player_instance: Players,
        player_manager_instance: PlayerManager,
    ):
        self.game = game_instance
        self.players = player_instance
        self.player_manager = player_manager_instance

    def start_game(self):
        pass

    def exit_game(self):
        pass

    def restart_game(self):
        pass

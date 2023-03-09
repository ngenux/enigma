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
        #Display the Game introduction
        intro = IntroDisplay()
        intro.show_game_intro()
        intro.explain_game_rules()

        #Creating and initiliazing players and recording their data
        players = Players()
        player_manager = PlayerManager(players)
        player_manager.get_player_names()
        player_manager.get_player_colors()
        player_manager.greet_players()
        player_manager.initialize_player_scores()

        while True:
            game = Game()
            game_option = GameOptionManager(player_manager)
            

    

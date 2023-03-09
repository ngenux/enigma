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
            game_option.start_game()

            player_manager.get_mark_colors()
            player_manager.get_player_marks()

            game_display = GameDisplay(game, players)
            game_manager = GameManager(game_display)

            players.player_scores = game_manager.game_loop(round)

            console.print(Text("SCORES:", style="green"),
                        Text(f"{players.player_names[0]}-{players.player_scores[0]}",style=players.player_colors[0],),
                        Text("AND", style="green"),
                        Text(f"{players.player_names[1]}-{players.player_scores[1]}",style=players.player_colors[1],),
                        )

            if game_manager.game_over():
                console.print('Gear up for another round!', style = 'green')
                round += 1
                continue
            break

        if game_option.exit_game():
            quit()
        else:
            game_option.restart_game()

           
            

            

    

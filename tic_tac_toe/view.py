from utils import console
from rich.markdown import Markdown
from rich.text import Text


class IntroDisplay:
    def __init__(self):
        self.banner = Markdown(
            """
            ```
              ________________            _________   ______            __________  ______
             /_  __/  _/ ____/           /_  __/   | / ____/           /_  __/ __ \/ ____/
              / /  / // /      ______     / / / /| |/ /      ______     / / / / / / __/   
             / / _/ // /___   /_____/    / / / ___ / /___   /_____/    / / / /_/ / /___   
            /_/ /___/\____/             /_/ /_/  |_\____/             /_/  \____/_____/   
                                                                                    
            ```
            Developed by Team ENIGMA
            """
        )

        self.rule_title = Text(
            " RULES OF THE GAME ", style="bold bright_red on bright_yellow"
        )
        self.rules = [
            "  + The starting player is chosen at random through a shuffle.",
            "  + The player can select their mark from the options of 'X' or 'O'.",
            "  + Each player will take turns to mark their position on the board.",
            "  + The winner is the first player to get three of their marks in a row, in any direction on the board.",
            "  + The game ends when all 9 squares on the board have been filled. If neither player has 3 marks in a row, the game results in a tie.",
        ]

    def show_game_intro(self):
        console.print(self.banner, style="bold rgb(48,227,223) blink")
        console.print("\n")
        console.print("Let the Fun begins. :alien:", style="green")
        console.print("\n")

    def explain_game_rules(self):
        console.rule(self.rule_title, style="bright_yellow")
        console.print("\n")
        for rule in self.rules:
            console.print(rule, style="green")
        console.print("\n")

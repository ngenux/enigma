from rich.console import Console

class IntroDisplay:

    def __init__(self):
        self.console = Console()


    def show_game_intro(self):

        # Print the banner message using the console.print() function
        # The message is in Markdown format and passed to the Markdown() function
        self.console.print(
            Markdown(
                """
        ````
        ________________            _________   ______            __________  ______
        /_  __/  _/ ____/           /_  __/   | / ____/           /_  __/ __ \/ ____/
        / /  / // /      ______     / / / /| |/ /      ______     / / / / / / __/   
        / / _/ // /___   /_____/    / / / ___ / /___   /_____/    / / / /_/ / /___   
        /_/ /___/\____/             /_/ /_/  |_\____/             /_/  \____/_____/   
                                                                                
        ```
        Developed by Team ENIGMA
        """
            ),
            style="bold rgb(48,227,223) blink",
        )
        # Print new line
        self.console.print("\n")
        # Print the message
        self.console.print("Let the Fun begins. :alien:", style="green")




    def explain_game_rules(self):
        self.console.rule(
            Text(" RULES OF THE GAME ", style="bold bright_red on bright_yellow"),
            style="bright_yellow",
        )
        self.console.print(
            "  + The starting player is chosen randomly by rolling a die. The player with the highest roll goes first.",
            style="green",
        )
        self.console.print(
            "  + Starting player is also given the option to choose their mark, either 'X' or 'O'.",
            style="green",
        )
        self.console.print(
            "  + Each player will get a chance to mark his position on the board in turns.",
            style="green",
        )
        self.console.print(
            "  + The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.",
            style="green",
        )
        self.console.print(
            "  + When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n",
            style="green",
        )
from typing import List, Tuple, Union
import random, sys, colorsys, time
from rich.console import Console

console = Console()

class GameTools:
    @staticmethod
    def generate_colors(number=2) -> List[str]:
        colors = []
        for _ in range(number):
            h, s, l = (
                random.random(),
                0.5 + random.random() / 2.0,
                0.4 + random.random() / 5.0,
            )
            r, g, b = [int(256 * i) for i in colorsys.hls_to_rgb(h, l, s)]
            colors.append(str(f"rgb({r},{g},{b})"))
        return colors

    @staticmethod
    def animate_shuffle(num_of_rolls=2) -> None:
        for i in range(num_of_rolls * 4):
            if i % 4 == 0:
                sys.stdout.write("\rShuffling Players |")
            elif i % 4 == 1:
                sys.stdout.write("\rShuffling Players /")
            elif i % 4 == 2:
                sys.stdout.write("\rShuffling Players -")
            else:
                sys.stdout.write("\rShuffling Players \\")
            sys.stdout.flush()
            time.sleep(0.5)
        sys.stdout.write("\rDone!    ")
        sys.stdout.write("\033[K")
        sys.stdout.write("\n")
        sys.stdout.flush()

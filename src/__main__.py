import time
import arcade
from . import game_of_life

SQR_LEN = 16
SCREEN_LEN = 512

LIST_LEN = SCREEN_LEN // SQR_LEN
EDGE = SQR_LEN // 8


class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_LEN, SCREEN_LEN, "Conway's Game of Life")
        arcade.set_background_color(arcade.color.WHITE)
        self.squares = [[0] * LIST_LEN for _ in range(LIST_LEN)]

        # glider
        self.squares[10][10] = 1
        self.squares[10][11] = 1
        self.squares[10][12] = 1
        self.squares[11][12] = 1
        self.squares[12][11] = 1
        
        # block
        self.squares[0][0] = 1
        self.squares[0][-1] = 1
        self.squares[-1][0] = 1
        self.squares[-1][-1] = 1
        self.paused: bool = True


    def on_draw(self):
        arcade.start_render()
        for y in range(LIST_LEN):
            my = map_sc(y)
            for x in range(LIST_LEN):
                mx = map_sc(x)
                if self.squares[y][x] == 1:
                    arcade.draw_lrtb_rectangle_filled(
                        mx + EDGE,
                        mx + SQR_LEN - EDGE,
                        my + SQR_LEN - EDGE,
                        my + EDGE,
                        arcade.color.BLACK,
                    )
        if not self.paused:
            self.squares = game_of_life.step(self.squares)
        time.sleep(.1)


def map_sc(n: int) -> int:
    return (n - LIST_LEN // 2) * SQR_LEN + SCREEN_LEN // 2


window = Game()
arcade.run()


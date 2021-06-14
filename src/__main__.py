import time
import arcade
from . import game_of_life
from .constants import *


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

        self.pause_button = arcade.Sprite(
            "src/ui/play.png",
            scale=0.08,
            center_x=SCREEN_LEN - 60,
            center_y=SCREEN_LEN - 35,
        )

        self.edit_button = arcade.Sprite(
            "src/ui/edit.png",
            scale=0.05,
            center_x=SCREEN_LEN - 120,
            center_y=SCREEN_LEN - 35,
        )

        self.prev_drawn_squares: dict[tuple[int, int], arcade.Sprite] = {}

        self.paused: bool = False
        self.editing: bool = False

    def on_draw(self):
        arcade.start_render()
        self.pause_button.draw()
        self.edit_button.draw()
        square_sprites = arcade.SpriteList(is_static=True)
        for y in range(LIST_LEN):
            my = map_sc(y)
            for x in range(LIST_LEN):
                if self.squares[y][x] == 1:
                    mx = map_sc(x)
                    if (mx, my) in self.prev_drawn_squares:
                        square_sprites.append(self.prev_drawn_squares[mx, my])
                    else:
                        square = create_square_at_loc(mx, my)
                        self.prev_drawn_squares[mx, my] = square
                        square_sprites.append(square)
        square_sprites.draw()
        if not self.paused:
            self.squares = game_of_life.step(self.squares)
        time.sleep(0.1)

    def on_mouse_press(self, x, y, _button, _modifiers):
        if (
            self.pause_button.left <= x <= self.pause_button.right
            and self.pause_button.bottom <= y <= self.pause_button.top
        ):
            self.paused = not self.paused
            if not self.paused:
                self.editing = False
        elif (
            self.edit_button.left <= x <= self.edit_button.right
            and self.edit_button.bottom <= y <= self.edit_button.top
        ):
            if self.paused:
                self.editing = True
        elif self.editing:
            i = y // 16
            j = x // 16
            self.squares[i][j] = not self.squares[i][j]


def map_sc(n: int) -> int:
    return (n - LIST_LEN // 2) * SQR_LEN + SCREEN_LEN // 2


def create_square_at_loc(x: int, y: int) -> arcade.Sprite:
    sqr = arcade.SpriteSolidColor(SQR_LEN - EDGE, SQR_LEN - EDGE, arcade.color.BLACK)
    sqr.center_x = x + SQR_LEN // 2
    sqr.center_y = y + SQR_LEN // 2
    return sqr


window = Game()
arcade.run()

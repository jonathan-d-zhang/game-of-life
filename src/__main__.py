import time
import arcade
from . import game_of_life
from .constants import *


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_LEN, WINDOW_LEN, "Conway's Game of Life")
        arcade.set_background_color(arcade.color.ASH_GREY)
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

        self.edit_button = arcade.Sprite(
            "src/images/edit.png",
            scale=0.05,
            center_x=WINDOW_LEN - 110,
            center_y=WINDOW_LEN - 32,
        )

        self.exit_button = arcade.Sprite(
            "src/images/exit.png",
            scale=0.30,
            center_x=WINDOW_LEN - 50,
            center_y=WINDOW_LEN - 32,
        )

        self.editing: bool = False

        self.lru = []

    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_filled(
            center_x=WINDOW_LEN // 2,
            center_y=WINDOW_LEN // 2,
            width=SCREEN_LEN,
            height=SCREEN_LEN,
            color=arcade.color.WHITE,
        )

        for y in range(LIST_LEN):
            my = map_sc(y)
            for x in range(LIST_LEN):
                mx = map_sc(x)
                if self.squares[y][x]:
                    arcade.draw_lrtb_rectangle_filled(
                        mx + EDGE,
                        mx + SQR_LEN - EDGE,
                        my + SQR_LEN - EDGE,
                        my + EDGE,
                        arcade.color.BLACK,
                    )

        if self.editing:
            self.draw_infobox("EDITING")

        self.edit_button.draw()
        self.exit_button.draw()

        if not self.editing:
            self.squares = game_of_life.step(self.squares)

        time.sleep(0.1)

    def on_mouse_press(self, x, y, _button, _modifiers):
        if (
            self.edit_button.left <= x <= self.edit_button.right
            and self.edit_button.bottom <= y <= self.edit_button.top
        ):
            self.editing = not self.editing
        elif (
            self.exit_button.left <= x <= self.exit_button.right
            and self.exit_button.bottom <= y <= self.exit_button.top
        ):
            arcade.window_commands.close_window()

        elif self.editing:
            i = int(y / SQR_LEN)
            j = int(x / SQR_LEN)
            self.squares[i][j] = not self.squares[i][j]

    def draw_infobox(self, text: str) -> None:
        arcade.draw_rectangle_outline(
            center_x=WINDOW_LEN // 2,
            center_y=WINDOW_LEN * 0.05,
            width=SCREEN_LEN // 3,
            height=30,
            color=arcade.color.BLACK,
        )
        arcade.draw_text(
            text,
            WINDOW_LEN // 2,
            WINDOW_LEN * 0.05,
            arcade.color.BLACK,
            20,
            anchor_x="center",
            anchor_y="center",
        )

#    def on_mouse_drag(self, x, y, dx, dy, _buttons, _modifiers):
#        if self.editing:
#            i = int((y + dy) / 16)
#            j = int((x + dx) / 16)
#            if (i, j) not in self.lru:
#                self.squares[i][j] = not self.squares[i][j]
#            if len(self.lru) == 2:
#                self.lru.pop(0)
#            self.lru.append((i, j))


def map_sc(n: int) -> int:
    return (n - LIST_LEN // 2) * SQR_LEN + int((WINDOW_LEN - SCREEN_LEN) * 2.5)


window = Game()
arcade.run()

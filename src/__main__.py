import arcade
from . import game_of_life

SQR_LEN = 10
SCREEN_LEN = 512

LIST_LEN = 15

squares = [[0] * LIST_LEN for _ in range(LIST_LEN)]

squares[5][5] = 1
squares[5][6] = 1
squares[5][7] = 1
squares[4][7] = 1
squares[3][6] = 1


def map_sc(n: int) -> int:
    return n * SQR_LEN + SCREEN_LEN // 2


def draw(_):
    global squares
    arcade.start_render()
    squares = game_of_life.step(squares)
    for y in range(LIST_LEN):
        for x in range(LIST_LEN):
            if squares[y][x] == 1:
                arcade.draw_lrtb_rectangle_filled(
                    map_sc(x),
                    map_sc(x) + SQR_LEN,
                    map_sc(y) + SQR_LEN,
                    map_sc(y),
                    arcade.color.BLACK,
                )
                arcade.draw_lrtb_rectangle_outline(
                    map_sc(x),
                    map_sc(x) + SQR_LEN,
                    map_sc(y) + SQR_LEN,
                    map_sc(y),
                    arcade.color.BLACK,
                )


arcade.open_window(SCREEN_LEN, SCREEN_LEN, "test")
arcade.set_background_color(arcade.color.WHITE)
arcade.schedule(draw, 0.25)
arcade.run()

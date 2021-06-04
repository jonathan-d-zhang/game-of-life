import arcade
from . import game_of_life

SQR_LEN = 16
SCREEN_LEN = 512

LIST_LEN = SCREEN_LEN // SQR_LEN

squares = [[0] * LIST_LEN for _ in range(LIST_LEN)]

# glider
squares[10][10] = 1
squares[10][11] = 1
squares[10][12] = 1
squares[11][12] = 1
squares[12][11] = 1

# block
squares[0][0] = 1
squares[0][-1] = 1
squares[-1][0] = 1
squares[-1][-1] = 1


def map_sc(n: int) -> int:
    return (n - LIST_LEN // 2) * SQR_LEN + SCREEN_LEN // 2


def draw(_):
    global squares
    arcade.start_render()
    for y in range(LIST_LEN):
        my = map_sc(y)
        for x in range(LIST_LEN):
            mx = map_sc(x)
            if squares[y][x] == 1:
                arcade.draw_lrtb_rectangle_filled(
                    mx,
                    mx + SQR_LEN,
                    my + SQR_LEN,
                    my,
                    arcade.color.BLACK,
                )
                arcade.draw_lrtb_rectangle_outline(
                    mx,
                    mx + SQR_LEN,
                    my + SQR_LEN,
                    my,
                    arcade.color.WHITE,
                )
    squares = game_of_life.step(squares)


arcade.open_window(SCREEN_LEN, SCREEN_LEN, "test")
arcade.set_background_color(arcade.color.WHITE)
arcade.schedule(draw, 0.1)
arcade.run()

import arcade
from . import game_of_life

SQR_LEN = 10
SCREEN_LEN = 512

squares = [
    (0, 0),
    (1, 0),
    (2, 0),
    (2, 1),
    (1, 2),
]


def draw(_):
    global squares
    arcade.start_render()
    squares = game_of_life.step(squares)
    for x, y in squares:
        x = x * SQR_LEN + SCREEN_LEN // 2
        y = y * SQR_LEN + SCREEN_LEN // 2
        arcade.draw_lrtb_rectangle_filled(
            x, x + SQR_LEN, y + SQR_LEN, y, arcade.color.BLACK
        )
        arcade.draw_lrtb_rectangle_outline(
            x, x + SQR_LEN, y + SQR_LEN, y, arcade.color.WHITE
        )


arcade.open_window(SCREEN_LEN, SCREEN_LEN, "test")
arcade.set_background_color(arcade.color.WHITE)
arcade.schedule(draw, 0.25)
arcade.run()

from random import randrange
import arcade

SQR_LEN = 10
SCREEN_LEN = 512

class Square:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __iter__(self):
        return iter((self.x, self.y))

squares = set()
for _ in range(15):
    x = randrange(-15, 15)
    y = randrange(-15, 15)
    squares.add(Square(x, y))
def draw(delta):
    arcade.start_render()
    for x, y in squares:
        x *= SQR_LEN
        y *= SQR_LEN
        x += SCREEN_LEN // 2
        y += SCREEN_LEN // 2
        arcade.draw_lrtb_rectangle_filled(x, x + SQR_LEN, y + SQR_LEN, y, arcade.color.BLACK)
    squares.add(Square(randrange(-15, 15), randrange(-15, 15)))
arcade.open_window(SCREEN_LEN, SCREEN_LEN, "test")
arcade.set_background_color(arcade.color.WHITE)
arcade.schedule(draw, 0.5)
arcade.run()

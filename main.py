from random import randrange
import arcade

SQR_LEN = 10
SCREEN_LEN = 512

squares = {(0, 0), (0, 1), (0, 2)}


def neighbors(tile, with_self=False):
    if with_self:
        yield tile

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 == dy:
                continue
            yield tile[0] + dx, tile[1] + dy


def update():
    seen = set()
    flipped = set()
    for tile in squares:
        for neighbor in neighbors(tile, with_self=True):
            if neighbor in seen:
                continue
            seen.add(neighbor)

            s = sum(
                neighbors_neighbor in squares
                for neighbors_neighbor in neighbors(neighbor)
            )
            if (neighbor in squares and (s != 2 and s != 3)) or (
                neighbor not in squares and s == 3
            ):
                flipped.add(neighbor)

    squares.symmetric_difference_update(flipped)


def draw(delta):
    arcade.start_render()
    update()
    for x, y in squares:
        x *= SQR_LEN
        y *= SQR_LEN
        x += SCREEN_LEN // 2
        y += SCREEN_LEN // 2
        arcade.draw_lrtb_rectangle_filled(
            x, x + SQR_LEN, y + SQR_LEN, y, arcade.color.BLACK
        )


arcade.open_window(SCREEN_LEN, SCREEN_LEN, "test")
arcade.set_background_color(arcade.color.WHITE)
arcade.schedule(draw, 0.01)
arcade.run()

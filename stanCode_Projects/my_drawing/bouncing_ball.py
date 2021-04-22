"""
File: bouncing_ball.py
Name: Amber Chang
-------------------------
This program simulates a bouncing ball.
The ball will bounce from the starting
point with the given horizontal velocity
and vertical velocity.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


# This constant controls when the program stops
TIMES = 3


# Global Variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
times = 0
# The times of completing the bouncing process
start = False
# The switch of whether the bouncing process starts


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(bounce)


def bounce(mouse):
    global times
    global start
    if not start and times < TIMES:
        vy = GRAVITY
        # The initial y velocity
        start = True
        while True:
            if ball.x + ball.width >= window.width:
                break
            else:
                if ball.y + ball.height >= window.height:
                    vy *= REDUCE
                    vy = -vy
                ball.move(VX, vy)
                vy += GRAVITY
                pause(DELAY)
        window.add(ball, x=START_X, y=START_Y)
        start = False
        times += 1


if __name__ == "__main__":
    main()

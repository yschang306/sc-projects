"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
----------------------------------------
File: breakout.py
Name: Amber Chang
----------------------------------------
This program will display the Breakout clone
game. When the ball touches the paddle or wall,
it will rebound, whereas when the ball touches
the brick, it will remove the brick and rebound.
Each player only has certain lives.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = 0
    # The lives that player loses
    bricks_left = graphics.get_brick_number()
    # The number of bricks left
    finish_game = False
    # This variable tells that whether the player break all the bricks

    # Add animation loop here!
    while True:
        if not finish_game and lives < NUM_LIVES:
            if graphics.get_start():
                graphics.set_start(False)
                dx = graphics.get_dx()
                # The initial x velocity
                dy = graphics.get_dy()
                # The initial y velocity
                paddle_touch = 0
                while True:
                    # Ball move
                    graphics.ball.move(dx, dy)

                    # Check collision
                    graphics.check_collision()
                    if graphics.obj is graphics.paddle:
                        paddle_touch += 1
                        # if graphics.ball.y + graphics.ball.height > graphics.paddle.y:
                        #     residual_y = graphics.ball.y + graphics.ball.height - graphics.paddle.y
                        #     # The difference between the bottom of the ball and the top of the paddle
                        #     graphics.ball.move(0, -residual_y)
                        #     # Moving the ball onto the top of the paddle
                        # dy *= -1
                        if paddle_touch == 1:
                            dy *= -1
                        else:
                            dy = dy
                    elif graphics.obj is not None:
                        dy *= -1
                        graphics.window.remove(graphics.obj)
                        bricks_left -= 1
                        paddle_touch = 0

                    # Check whether there is no bricks
                    if bricks_left == 0:
                        finish_game = True
                        break

                    # Check whether there is a wall
                    if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                        dx *= -1
                    if graphics.ball.y <= 0:
                        dy *= -1

                    # Check whether the ball falls out of the window bottom
                    if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                        lives += 1
                        break

                    # Pause
                    pause(FRAME_RATE)
                graphics.window.add(graphics.ball, graphics.get_ball_x(), graphics.get_ball_y())
            pause(FRAME_RATE)

        elif finish_game or lives == NUM_LIVES:
            break


if __name__ == '__main__':
    main()

"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
----------------------------------------
File: breakout_extensions.py
Name: Amber Chang
----------------------------------------
This program will display the Breakout clone
game. When the ball touches the paddle or wall,
it will rebound, whereas when the ball touches
the brick, it will remove the brick and rebound.
Each player only has certain lives. Each brick
has different score, such as 1, 5, 10, 15, 25
points.
"""

from campy.gui.events.timer import pause
from campy.graphics.gobjects import GOval
from breakoutgraphics_extensions import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    score = graphics.get_score()
    # The initial score
    lives = 0
    # The lives that player loses
    bricks_left = graphics.get_brick_number()
    # The number of bricks left
    finish_game = False
    # This variable tells that whether the player break all the bricks

    # The visualized lives
    space = 10
    x = graphics.window.width
    y = graphics.window.height - space - graphics.get_ball_2r()
    for i in range(NUM_LIVES - 1):
        lives_left = GOval(graphics.get_ball_2r(), graphics.get_ball_2r())
        lives_left.filled = True
        lives_left.fill_color = 'black'
        x -= (lives_left.width + space)
        graphics.window.add(lives_left, x, y)

    # Add animation loop here!
    while True:
        if not finish_game and lives < NUM_LIVES:
            if graphics.get_start():
                graphics.window.remove(graphics.get_start_instruction())
                graphics.set_start(False)
                dx = graphics.get_dx()
                dy = graphics.get_dy()
                while True:
                    # Ball move
                    graphics.ball.move(dx, dy)

                    # Check collision
                    graphics.check_collision()
                    if graphics.obj is graphics.paddle:
                        if graphics.ball.y + graphics.ball.height > graphics.paddle.y:
                            residual_y = graphics.ball.y + graphics.ball.height - graphics.paddle.y
                            # The difference between the bottom of the ball and the top of the paddle
                            graphics.ball.move(0, -residual_y)
                            # Moving the ball onto the top of the paddle
                        dy *= -1
                    elif graphics.obj is not None:
                        # Identify the object above the paddle to avoid removing the score board and visualized lives
                        if graphics.ball.y + graphics.ball.height < graphics.paddle.y:
                            dy *= -1
                            graphics.window.remove(graphics.obj)
                            bricks_left -= 1
                            graphics.score_count()
                            # Identify the score level of the removed brick
                            score += graphics.get_score_level()
                            graphics.score_board.text = 'Score: '+str(score)

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
                        if lives == 1:
                            x += graphics.ball.width / 2
                            lives_ball = graphics.window.get_object_at(x, y)
                        else:
                            x += graphics.get_ball_2r() + space
                            lives_ball = graphics.window.get_object_at(x, y)
                        graphics.window.remove(lives_ball)
                        break

                    # Pause
                    pause(FRAME_RATE)

                graphics.window.add(graphics.ball, graphics.get_ball_x(), graphics.get_ball_y())
            pause(FRAME_RATE)

        elif finish_game:
            graphics.finish_game()
            break
        elif lives == NUM_LIVES:
            for i in range(8):
                graphics.fail_game1()
                pause(FRAME_RATE * 6)
                graphics.fail_game2()
                pause(FRAME_RATE * 6)
            break


if __name__ == '__main__':
    main()

"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
----------------------------------------
File: breakoutgraphics_extensions.py
Name: Amber Chang
----------------------------------------
This class will create the graphics of the
Breakout clone game, which consists of a
ball, a paddle, s score board and bricks.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        paddle_x = (self.window.width - self.paddle.width) / 2
        # The initial x coordinate of the paddle
        self.__paddle_y = self.window.height - self.paddle.height - paddle_offset
        # The permanent y coordinate of the paddle
        self.window.add(self.paddle, paddle_x, self.__paddle_y)

        # Center a filled ball in the graphical window
        self.__ball_2r = ball_radius * 2
        self.ball = GOval(self.__ball_2r, self.__ball_2r)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.__ball_x = (self.window.width - self.ball.width) / 2
        # The initial x coordinate of the ball
        self.__ball_y = (self.window.height - self.ball.height) / 2
        # The initial y coordinate of the ball
        self.window.add(self.ball, self.__ball_x, self.__ball_y)

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        self.__start = False
        # This variable that detects when the game starts
        onmouseclicked(self.start_game)

        # Draw bricks
        self.__brick_number = brick_rows * brick_cols
        self.__brick_y = brick_offset
        # The initial y coordinate of the brick
        for i in range(brick_rows):
            self.__brick_x = 0
            # The initial x coordinate of the brick
            if i > 0:
                self.__brick_y = self.__brick_y + self.__brick.height + brick_spacing
            for j in range(brick_cols):
                self.__brick = GRect(brick_width, brick_height)
                self.__brick.filled = True
                if i <= 1:
                    self.__brick.fill_color = 'red'
                    self.__brick.color = 'red'
                elif i <= 3:
                    self.__brick.fill_color = 'orange'
                    self.__brick.color = 'orange'
                elif i <= 5:
                    self.__brick.fill_color = 'yellow'
                    self.__brick.color = 'yellow'
                elif i <= 7:
                    self.__brick.fill_color = 'green'
                    self.__brick.color = 'green'
                else:
                    self.__brick.fill_color = 'blue'
                    self.__brick.color = 'blue'
                self.window.add(self.__brick, self.__brick_x, self.__brick_y)
                self.__brick_x = self.__brick_x + brick_width + brick_spacing

        # Check collision
        self.obj = None
        # The object that the ball touches
        self.check_collision()

        # Start instruction
        self.__start_instruction = GLabel('Click to start the game')
        self.__start_instruction.font = '-15-italic'
        self.window.add(self.__start_instruction, (self.window.width - self.__start_instruction.width) / 2,
                        self.ball.y + self.ball.height + 25)

        # Score board
        self.__score = 0
        # The initial score
        self.score_board = GLabel('Score: ' + str(self.__score))
        self.score_board.font = '-25'
        self.window.add(self.score_board, 5, self.window.height)
        self.__brick_offset = brick_offset
        self.__brick_height = brick_height
        self.__brick_spacing = brick_spacing
        self.__score_level = 0

    # score getter
    def get_score(self):
        return self.__score

    def score_count(self):
        if self.obj is not None:
            if self.__brick_offset == self.obj.y:
                self.__score_level = 25
            elif self.__brick_offset + self.__brick_height + self.__brick_spacing == self.obj.y:
                self.__score_level = 25
            elif self.__brick_offset + 2 * self.__brick_height + 2 * self.__brick_spacing == self.obj.y:
                self.__score_level = 15
            elif self.__brick_offset + 3 * self.__brick_height + 3 * self.__brick_spacing == self.obj.y:
                self.__score_level = 15
            elif self.__brick_offset + 4 * self.__brick_height + 4 * self.__brick_spacing == self.obj.y:
                self.__score_level = 10
            elif self.__brick_offset + 5 * self.__brick_height + 5 * self.__brick_spacing == self.obj.y:
                self.__score_level = 10
            elif self.__brick_offset + 6 * self.__brick_height + 6 * self.__brick_spacing == self.obj.y:
                self.__score_level = 5
            elif self.__brick_offset + 7 * self.__brick_height + 7 * self.__brick_spacing == self.obj.y:
                self.__score_level = 5
            elif self.__brick_offset + 8 * self.__brick_height + 8 * self.__brick_spacing == self.obj.y:
                self.__score_level = 1
            elif self.__brick_offset + 9 * self.__brick_height + 9 * self.__brick_spacing == self.obj.y:
                self.__score_level = 1

    # score_level getter
    def get_score_level(self):
        return self.__score_level

    # start_instruction getter
    def get_start_instruction(self):
        return self.__start_instruction

    # ball diameter getter
    def get_ball_2r(self):
        return self.__ball_2r

    # ball_x and ball_y getter
    def get_ball_x(self):
        return self.__ball_x

    def get_ball_y(self):
        return self.__ball_y

    # dx and dy getters
    def get_dx(self):
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    def get_dy(self):
        return self.__dy

    # brick number getter
    def get_brick_number(self):
        return self.__brick_number

    # start getter
    def get_start(self):
        return self.__start

    # start setter
    def set_start(self, new_start):
        self.__start = new_start

    def start_game(self, click):
        if self.ball.x != self.__ball_x and self.ball.y != self.__ball_y:
            self.__start = False
        else:
            self.__start = True

    # Check whether the ball touches object
    def check_collision(self):
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
            self.obj = self.window.get_object_at(self.ball.x, self.ball.y)
        elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y) is not None:
            self.obj = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        elif self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height) is not None:
            self.obj = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height) is not None:
            self.obj = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        else:
            self.obj = None
        return self.obj

    # The paddle moves as the mouse moves
    def move_paddle(self, mouse):
        paddle_move_left_x = mouse.x - self.paddle.width / 2
        # The left-sided x coordinate of the paddle as moving the mouse
        paddle_move_right_x = mouse.x + self.paddle.width / 2
        # The right-sided x coordinate of the paddle as moving the mouse
        if 0 <= paddle_move_left_x and paddle_move_right_x <= self.window.width:
            self.window.add(self.paddle, paddle_move_left_x, self.__paddle_y)

    def fail_game1(self):
        fail_frame = GRect(450, 80)
        fail_frame.filled = True
        fail_frame.fill_color = 'gray'
        fail_frame.color = 'gray'
        self.window.add(fail_frame, (self.window.width - fail_frame.width) / 2,
                            (self.window.height - fail_frame.height)/ 2)
        failed = GLabel('Game Over')
        failed.font = '-60-bold'
        failed.color = 'white'
        self.window.add(failed, fail_frame.x + 70, fail_frame.y + 75)

    def fail_game2(self):
        fail_frame = GRect(450, 80)
        fail_frame.filled = True
        fail_frame.fill_color = 'white'
        fail_frame.color = 'white'
        self.window.add(fail_frame, (self.window.width - fail_frame.width) / 2,
                            (self.window.height - fail_frame.height)/ 2)
        failed = GLabel('Game Over')
        failed.font = '-60-bold'
        failed.color = 'black'
        self.window.add(failed, fail_frame.x + 70, fail_frame.y + 75)

    def finish_game(self):
        finish_frame = GRect(450, 80)
        finish_frame.filled = True
        finish_frame.fill_color = 'white'
        finish_frame.color = 'white'
        self.window.add(finish_frame, (self.window.width - finish_frame.width) / 2, (self.window.height -
                                                                                         finish_frame.height) / 2)
        finish = GLabel('Congratulation!!! You win!')
        finish.font = '-35-bold'
        finish.color = 'red'
        self.window.add(finish, finish_frame.x + 10, finish_frame.y + 65)

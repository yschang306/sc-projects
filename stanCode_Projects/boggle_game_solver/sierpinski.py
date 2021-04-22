"""
File: sierpinski.py
Name: Amber Chang
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	This program draws the Sierpinski triangle of
	a given order.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: The order left of the Sierpinski Triangle
	:param length: The length of each order of the Sierpinski Triangle
	:param upper_left_x: The upper left x coordinate of each triangle
	:param upper_left_y: The upper left y coordinate of each triangle
	:return: The Sierpinski Triangle of the given order
	"""
	if order == 0:
		return
	else:
		left_side = GLine(upper_left_x, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)
		window.add(left_side)
		right_side = GLine(upper_left_x+length*0.5, upper_left_y+length*0.866, upper_left_x+length, upper_left_y)
		window.add(right_side)
		upper_side = GLine(upper_left_x+length, upper_left_y, upper_left_x, upper_left_y)
		window.add(upper_side)
		# Draw a triangle
		sierpinski_triangle(order-1, length*0.5, upper_left_x, upper_left_y)
		# Add the upper left triangle
		sierpinski_triangle(order-1, length*0.5, upper_left_x+length*0.5, upper_left_y)
		# Add the upper right triangle
		sierpinski_triangle(order-1, length*0.5, upper_left_x+length*0.5*0.5, upper_left_y+length*0.5*0.866)
		# Add the bottom triangle


if __name__ == '__main__':
	main()

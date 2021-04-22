"""
File: draw_line.py
Name: Amber Chang
-------------------------------------
This file shows how to use campy mouse
to draw lines(GLine) on the window where
two points of the line are randomly chosen.
The first click will create a circle shown
on the window whereas the second one won't
and in the meantime the initial circle will
disappear, meaning there is only a line once
the user clicks for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


# This constant controls the size of the circle
SIZE = 20

# Global Variables
window = GWindow()
click = 0
pre_x = 0
# The x coordinate of the first click
pre_y = 0
# The y coordinate of the first click


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(m):
    global click
    global pre_x
    global pre_y
    click += 1
    if click % 2 == 1:
        circle = GOval(SIZE, SIZE)
        window.add(circle, m.x - circle.width / 2, m.y - circle.height / 2)
        pre_x = m.x
        pre_y = m.y
    else:
        pre_circle = window.get_object_at(pre_x, pre_y)
        # The circle created at the first click
        window.remove(pre_circle)
        line = GLine(x0=pre_x, x1=m.x, y0=pre_y, y1=m.y)
        window.add(line)


if __name__ == "__main__":
    main()

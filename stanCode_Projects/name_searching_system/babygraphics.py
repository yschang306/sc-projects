"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
-----------------------------------------------------
File: babygraphics.py
Name: Amber Chang
-----------------------------------------------------
This program draws the line chart of the change of
baby names' ranking over years as user input names
which he or she wants to check.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    avg_distance = (width - 2 * GRAPH_MARGIN_SIZE) // len(YEARS)
    # The average distance between x coordinates of each vertical line representing the year
    x_coordinate = GRAPH_MARGIN_SIZE + avg_distance * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # The top horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    # The bottom horizontal line
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        line_color = COLORS[i % len(COLORS)]
        ranks = []
        # The ranking of every year
        for year in YEARS:
            if str(year) in name_data[name]:
                ranks.append(name_data[name][str(year)])
            else:
                ranks.append('*')

        pre_x = 0
        # The x coordinate of the former year
        pre_y = 0
        # The y coordinate of the former year
        for j in range(len(ranks)):
            rank = ranks[j]
            x = get_x_coordinate(CANVAS_WIDTH, j)
            # The x coordinate of current year that is drawn
            if rank == '*':
                y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                # The y coordinate of current year that is drawn
                # If the rank is out of 1000, representing by '*', the y coordinate will on the bottom horizontal line
            else:
                y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK * (int(rank) - 1)
                # (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK is the unit interval of vertical lines
                # When rank equals to 1, the y coordinate is the margin size
            canvas.create_text(x + TEXT_DX, y, text=f'{name} {rank}', anchor=tkinter.SW, fill=line_color)
            if j > 0:
                canvas.create_line(pre_x, pre_y, x, y, width=LINE_WIDTH, fill=line_color)
                # Create the line when there are two points, the previous rank and the current rank being drawn
            pre_x = x
            pre_y = y


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()

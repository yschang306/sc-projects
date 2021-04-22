"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    This function will replace the green pixels of the figure image
    with the pixels of background image
    ---------------------------------------------
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, the green screen figure image
    :return: SimpleImage, the combined image of the figure and background image
    """
    background_img.make_as_big_as(figure_img)
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            fig_pixel = figure_img.get_pixel(x, y)
            bigger = max(fig_pixel.red, fig_pixel.blue)
            # Returns the one that is bigger
            if fig_pixel.green > bigger * 2:
                bg_pixel = background_img.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
    return figure_img


def main():
    """
    This program will show the combined image after
    replacing the green parts of the figure image with
    the background image
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()

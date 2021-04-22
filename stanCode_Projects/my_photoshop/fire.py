"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    This function will highlight the fire in the image with red
    and turn the rest of it into gray
    -----------------------------------------------------------
    :param filename: str, the name of the file
    :return: SimpleImage, the image of highlighted fires
    """
    highlighted_img = SimpleImage(filename)
    for pixel in highlighted_img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
            # The pixel will become gray
    return highlighted_img


def main():
    """
    This program will show the original fire image
    and the highlighted fire image
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()

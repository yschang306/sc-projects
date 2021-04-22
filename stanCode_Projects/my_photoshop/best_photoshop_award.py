"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.4

# Controls the upper bound for black pixel
BLACK_PIXEL = 120


def combine(fg, bg):
    """
    This function will replace the green pixels of the figure image
    with the pixels of background image
    ---------------------------------------------
    : param1 fg: SimpleImage, the green screen figure image
    : param2 bg: SimpleImage, the background image
    : return fg: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for x in range(fg.width):
        for y in range(fg.height):
            pixel_fg = fg.get_pixel(x, y)
            avg = (pixel_fg.red + pixel_fg.blue + pixel_fg.green) // 3
            total = pixel_fg.red + pixel_fg.blue + pixel_fg.green
            if pixel_fg.green > avg * THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_fg.red = pixel_bg.red
                pixel_fg.green = pixel_bg.green
                pixel_fg.blue = pixel_bg.blue
    return fg


def main():
    """
    This program will replace the green screen
    which can photoshop a person onto any background
    -----------------------------------------------------------
    Concept: My face is round and I like to eat soft-boiled egg.
             As a result, I turn the egg yolk into my face, soaking
             in the ramen and feeling comfortable.
    """
    fg = SimpleImage('image_contest/me.jpg')
    bg = SimpleImage('image_contest/ramen.jpg')
    bg.make_as_big_as(fg)
    combined_img = combine(fg, bg)
    combined_img.show()


if __name__ == '__main__':
    main()

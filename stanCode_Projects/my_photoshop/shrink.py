"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    This function will shrink the original image
    into half of its original size
    ---------------------------------------------
    :param filename: str, the filename
    :return img: SimpleImage, the shrank image
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.width // 2, img.height // 2)
    for x in range(new_img.width):
        for y in range(new_img.height):
            img_p = img.get_pixel(x * 2, y * 2)
            new_img_p = new_img.get_pixel(x, y)

            new_img_p.red = img_p.red
            new_img_p.green = img_p.green
            new_img_p.blue = img_p.blue
    return new_img


def main():
    """
    This program will show the original image and the shrank image
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()

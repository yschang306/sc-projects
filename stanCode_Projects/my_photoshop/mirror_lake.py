"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    This function will create a reflected image in a vertical way
    -----------------------------------------------------------
    :param filename: str, the name of the file
    :return: SimpleImage, the reflected image
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.width, img.height * 2)
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)
            # The colored pixel of the original image
            new_img_pixel1 = new_img.get_pixel(x, y)
            # The blanked pixel of the new image counted from the top
            new_img_pixel2 = new_img.get_pixel(x, new_img.height - 1 - y)
            # The blanked pixel of the new image counted from the bottom
            new_img_pixel1.red = img_pixel.red
            new_img_pixel1.green = img_pixel.green
            new_img_pixel1.blue = img_pixel.blue

            new_img_pixel2.red = img_pixel.red
            new_img_pixel2.green = img_pixel.green
            new_img_pixel2.blue = img_pixel.blue
    return new_img


def main():
    """
    This program will show the original image
    and the image with mirror symmetry
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()

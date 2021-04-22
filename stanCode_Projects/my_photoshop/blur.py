"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    This function will blur the original image
    ---------------------------------------------
    :param img: SimpleImage, the original image
    :return: SimpleImage, the blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            img_p = img.get_pixel(x, y)
            new_img_p = new_img.get_pixel(x, y)
            if x == 0 and y == 0:
                # The pixel at the upper left corner
                img_p1 = img.get_pixel(x, y + 1)
                img_p2 = img.get_pixel(x + 1, y)
                img_p3 = img.get_pixel(x + 1, y + 1)
                new_img_p.red = (img_p.red + img_p1.red + img_p2.red + img_p3.red) // 4
                new_img_p.green = (img_p.green + img_p1.green + img_p2.green + img_p3.green) // 4
                new_img_p.blue = (img_p.blue + img_p1.blue + img_p2.blue + img_p3.blue) // 4
            elif x == 0 and y == new_img.height - 1:
                # The pixel at the bottom left corner
                img_p1 = img.get_pixel(x, y - 1)
                img_p2 = img.get_pixel(x + 1, y)
                img_p3 = img.get_pixel(x + 1, y - 1)
                new_img_p.red = (img_p.red + img_p1.red + img_p2.red + img_p3.red) // 4
                new_img_p.green = (img_p.green + img_p1.green + img_p2.green + img_p3.green) // 4
                new_img_p.blue = (img_p.blue + img_p1.blue + img_p2.blue + img_p3.blue) // 4
            elif x == new_img.width - 1 and y == 0:
                # The pixel at the upper right corner
                img_p1 = img.get_pixel(x, y + 1)
                img_p2 = img.get_pixel(x - 1, y)
                img_p3 = img.get_pixel(x - 1, y + 1)
                new_img_p.red = (img_p.red + img_p1.red + img_p2.red + img_p3.red) // 4
                new_img_p.green = (img_p.green + img_p1.green + img_p2.green + img_p3.green) // 4
                new_img_p.blue = (img_p.blue + img_p1.blue + img_p2.blue + img_p3.blue) // 4
            elif x == new_img.width - 1 and y == new_img.height - 1:
                # The pixel at the bottom right corner
                img_p1 = img.get_pixel(x, y - 1)
                img_p2 = img.get_pixel(x - 1, y)
                img_p3 = img.get_pixel(x - 1, y - 1)
                new_img_p.red = (img_p.red + img_p1.red + img_p2.red + img_p3.red) // 4
                new_img_p.green = (img_p.green + img_p1.green + img_p2.green + img_p3.green) // 4
                new_img_p.blue = (img_p.blue + img_p1.blue + img_p2.blue + img_p3.blue) // 4
            elif x == 0 and y < new_img.height - 1:
                # Pixels on the left edge
                img_p1 = img.get_pixel(x, y - 1)
                img_p2 = img.get_pixel(x, y + 1)
                img_p3 = img.get_pixel(x + 1, y)
                img_p4 = img.get_pixel(x + 1, y - 1)
                img_p5 = img.get_pixel(x + 1, y + 1)
                new_img_p.red = (img_p.red + img_p1.red + img_p2.red + img_p3.red + img_p4.red + img_p5.red) // 6
                new_img_p.green = (img_p.green + img_p1.green + img_p2.green + img_p3.green + img_p4.green
                                   + img_p5.green) // 6
                new_img_p.blue = (img_p.blue + img_p1.blue + img_p2.blue + img_p3.blue + img_p4.blue + img_p5.blue) // 6
            elif x == new_img.width - 1 and y < new_img.height - 1:
                # Pixels on the right edge
                img_p1 = img.get_pixel(x, y - 1)
                img_p2 = img.get_pixel(x, y + 1)
                img_p3 = img.get_pixel(x - 1, y)
                img_p4 = img.get_pixel(x - 1, y - 1)
                img_p5 = img.get_pixel(x - 1, y + 1)
                new_img_p.red = (img_p.red + img_p1.red + img_p2.red + img_p3.red + img_p4.red + img_p5.red) // 6
                new_img_p.green = (img_p.green + img_p1.green + img_p2.green + img_p3.green + img_p4.green
                                   + img_p5.green) // 6
                new_img_p.blue = (img_p.blue + img_p1.blue + img_p2.blue + img_p3.blue + img_p4.blue + img_p5.blue) // 6
            elif x < new_img.width - 1 and y == 0:
                # Pixels on the upper edge
                img_p1 = img.get_pixel(x, y + 1)
                img_p2 = img.get_pixel(x - 1, y)
                img_p3 = img.get_pixel(x - 1, y + 1)
                img_p4 = img.get_pixel(x + 1, y)
                img_p5 = img.get_pixel(x + 1, y + 1)
                new_img_p.red = (img_p.red + img_p1.red + img_p2.red + img_p3.red + img_p4.red + img_p5.red) // 6
                new_img_p.green = (img_p.green + img_p1.green + img_p2.green + img_p3.green + img_p4.green
                                   + img_p5.green) // 6
                new_img_p.blue = (img_p.blue + img_p1.blue + img_p2.blue + img_p3.blue + img_p4.blue + img_p5.blue) // 6
            elif x < new_img.width - 1 and y == new_img.height - 1:
                # Pixels on the bottom edge
                img_p1 = img.get_pixel(x, y - 1)
                img_p2 = img.get_pixel(x - 1, y)
                img_p3 = img.get_pixel(x - 1, y - 1)
                img_p4 = img.get_pixel(x + 1, y)
                img_p5 = img.get_pixel(x + 1, y - 1)
                new_img_p.red = (img_p.red + img_p1.red + img_p2.red + img_p3.red + img_p4.red + img_p5.red) // 6
                new_img_p.green = (img_p.green + img_p1.green + img_p2.green + img_p3.green + img_p4.green
                                   + img_p5.green) // 6
                new_img_p.blue = (img_p.blue + img_p1.blue + img_p2.blue + img_p3.blue + img_p4.blue + img_p5.blue) // 6
            else:
                # Pixels in the middle
                img_p1 = img.get_pixel(x, y - 1)
                img_p2 = img.get_pixel(x, y + 1)
                img_p3 = img.get_pixel(x - 1, y)
                img_p4 = img.get_pixel(x - 1, y - 1)
                img_p5 = img.get_pixel(x - 1, y + 1)
                img_p6 = img.get_pixel(x + 1, y)
                img_p7 = img.get_pixel(x + 1, y - 1)
                img_p8 = img.get_pixel(x + 1, y + 1)
                new_img_p.red = (img_p.red + img_p1.red + img_p2.red + img_p3.red + img_p4.red + img_p5.red +
                                 img_p6.red + img_p7.red + img_p8.red) // 9
                new_img_p.green = (img_p.green + img_p1.green + img_p2.green + img_p3.green + img_p4.green +
                                   img_p5.green + img_p6.green + img_p7.green + img_p8.green) // 9
                new_img_p.blue = (img_p.blue + img_p1.blue + img_p2.blue + img_p3.blue + img_p4.blue + img_p5.blue +
                                  img_p6.blue + img_p7.blue + img_p8.blue) // 9
    return new_img


def main():
    """
    This program will show the original image and the blurred image
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()

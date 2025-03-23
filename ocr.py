import skimage
import pytest
from matplotlib import pyplot as plt
from skimage.feature import match_template


def read_image(image_file_name):
    image = skimage.io.imread(image_file_name)

    return image


def crop_template_from_image(_image):
    # one
    # reading from matplotlib x and y are flipped:
    # UL (x, ) to UR (x, ) = ymin to ymax
    # UR ( ,y) to LR ( ,y) = xmin to xmax
    x_min, y_min = (690, 90)
    x_max, y_max = (720, 115)

    _template = _image[x_min:x_max, y_min:y_max]

    return _template


image_file_name = "/Users/mark/computer_vision_optical_character_recognition/source/Sample 1_page1.png"

image = read_image(image_file_name)
template = crop_template_from_image(image)


def test_image_read():
    x, y, d = image.shape
    print(x, y)
    plt.imshow(template)
    plt.show()

    plt.imshow(image)
    plt.show()

    return

def test_image_template_match():
    return
import skimage
import numpy
import pytest
from matplotlib import pyplot as plt
from skimage.feature import match_template


def read_image(image_file_name):
    image = skimage.io.imread(image_file_name)

    return image


def crop_template_from_image(_image, _template_coordinates_min, _template_coordinates_max):
    # one (double x to account for double digit numbers )
    # reading from matplotlib x and y are flipped:
    # UL (x, ) to UR (x, ) = ymin to ymax
    # UR ( ,y) to LR ( ,y) = xmin to xmax

    x_min, y_min = _template_coordinates_min
    x_max, y_max = _template_coordinates_max

    _template = _image[x_min:x_max, y_min:y_max]

    return _template

def extract_position(_image, _template):
    _result = match_template(image, template)
    ij = numpy.unravel_index(numpy.argmax(_result), _result.shape)  # referenced to (x_min, y_min)
    (x, y, d) = ij
    coordinate = (x, y)

    return coordinate


def output_positions(image_file_name, positions):
    image_title = (image_file_name.split("/"))[-1]

    print(image_title)
    print("Note: matching pixel coordinates given x_min , y_min")

    for i, coordinate in enumerate(positions):
        x, y = coordinate
        print(i+1,"at: ", x, ",", y)

    return

ONE_COORDINATES_MIN = (690, 90)
ONE_COORDINATES_MAX = (720, 140)

image_file_name = "/Users/mark/computer_vision_optical_character_recognition/source/Sample 1_page1.png"

image = read_image(image_file_name)
template = crop_template_from_image(image, ONE_COORDINATES_MIN, ONE_COORDINATES_MAX)

coordinate = extract_position(image, template)
output_positions(image_file_name, [coordinate, coordinate])


def test_image_read():
    x, y, d = image.shape
    print(x, y)
    plt.imshow(template)
    plt.show()

    plt.imshow(image)
    plt.show()

    return

def test_image_template_match():
    plt.imshow(result, cmap='magma')
    plt.show()
    return
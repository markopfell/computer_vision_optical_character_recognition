import skimage
import numpy
import pytest
from matplotlib import pyplot as plt
from skimage.feature import match_template


def read_image(image_file_name):
    image = skimage.io.imread(image_file_name)

    return image


def crop_template_from_image(_image, _template_coordinates_min, _template_coordinates_max):
    x_min, y_min = _template_coordinates_min
    x_max, y_max = _template_coordinates_max

    _template = _image[x_min:x_max, y_min:y_max]

    return _template

def extract_position(_image, _template):
    _result = match_template(image, _template)
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


def multiple_templates_positions(_templates_coordinates):
    _position_coordinates = []

    for _template_coordinates in _templates_coordinates:
        _coordinates_min, _coordinates_max = _template_coordinates
        _template = crop_template_from_image(image, _coordinates_min, _coordinates_max)
        _position_coordinates.append(extract_position(image, _template))

    return _position_coordinates


image_file_name = "/Users/mark/computer_vision_optical_character_recognition/source/Sample 1_page1.png"

image = read_image(image_file_name)

## TODO: Clean this up
# (double x to account for double digit numbers from single digit)
# reading from matplotlib x and y are flipped:
# UL (x, ) to UR (x, ) = ymin to ymax
# UR ( ,y) to LR ( ,y) = xmin to xmax
one_coordinates_min = (690, 90)
one_coordinates_max = (720, 140)
two_coordinates_min = (690, 90)
two_coordinates_max = (720, 140)
three_coordinates_min = (690, 90)
three_coordinates_max = (720, 140)

templates_coordinates = [[one_coordinates_min, one_coordinates_max],
                         [two_coordinates_min, two_coordinates_max],
                         [three_coordinates_min, three_coordinates_max]]
##

position_coordinates = multiple_templates_positions(templates_coordinates)
output_positions(image_file_name, position_coordinates)


def test_image_read():
    x, y, d = image.shape
    print(x, y)
    template = crop_template_from_image(image, one_coordinates_min, one_coordinates_max)

    plt.imshow(template)
    plt.show()

    plt.imshow(image)
    plt.show()

    return
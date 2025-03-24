import datetime
import skimage
import numpy
import timeit
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from matplotlib.pyplot import cm
from skimage.feature import match_template

def read_image(_image_file_name):
    _image = skimage.io.imread(_image_file_name)

    return _image


def crop_template_from_image(_image, _template_coordinates_min, _template_coordinates_max):
    x_min, y_min = _template_coordinates_min
    x_max, y_max = _template_coordinates_max

    _template = _image[x_min:x_max, y_min:y_max]

    return _template


def extract_position(_image, _template):
    _result = match_template(_image, _template)
    ij = numpy.unravel_index(numpy.argmax(_result), _result.shape)  # referenced to (x_min, y_min)
    (x, y, d) = ij
    coordinate = (x, y)

    return coordinate


def output_positions(_image_file_name, positions, _start_time):
    image_title = (_image_file_name.split("/"))[-1]

    _stop_time = timeit.default_timer()

    print('\n')
    print('------------------- Output start -------------------')
    print('Report date and time: ', datetime.datetime.now())
    print(image_title)
    print("Note: matching pixel coordinates given x_min , y_min\n")

    for i, coordinate in enumerate(positions):
        print(coordinate)
        x, y = coordinate
        print(i + 1, "at: ", x, ",", y)
    print('\nCompute time: ', round(_stop_time - _start_time, 1), 'sec')
    print('-------------------- Output end --------------------')

    return


def multiple_templates_positions(_templates_coordinates, _image, _template_image):
    _position_coordinates = []
    _templates = []

    for _template_coordinates in _templates_coordinates:
        _coordinates_min, _coordinates_max = _template_coordinates
        _template = crop_template_from_image(_template_image, _coordinates_min, _coordinates_max)
        _templates.append(_template)

        _position_coordinate = extract_position(_image, _template)
        _position_coordinates.append(_position_coordinate)

    return (_position_coordinates, _templates)


def manual_template_coordinates():
    # (double x to account for double-digit numbers from single digit)
    # reading from matplotlib x and y are flipped:
    # UL (x, ) to UR (x, ) = y_min to y_max
    # UR ( ,y) to LR ( ,y) = x_min to x_max
    one_coordinates_min = (690, 90)
    one_coordinates_max = (720, 140)
    two_coordinates_min = (680, 978)
    two_coordinates_max = (710, 1020)
    three_coordinates_min = (665, 1291)
    three_coordinates_max = (695, 1331)

    _templates_coordinates = [
        [one_coordinates_min, one_coordinates_max],
        [two_coordinates_min, two_coordinates_max],
        [three_coordinates_min, three_coordinates_max],
    ]
    ##

    return _templates_coordinates


def crop(_image, y_max):
    _cropped_image = _image[0:y_max, 0:_image.shape[1]]

    return _cropped_image


start_time = timeit.default_timer()
fig, ax = plt.subplots()

image_file_name = "/Users/mark/computer_vision_optical_character_recognition/source/Sample 1_page2.png"
template_image_file_name = "/Users/mark/computer_vision_optical_character_recognition/source/Sample 1_page1.png"

crop_y_max_pixel = 900  # Need this to prune the false positives from the legend in the document
image = read_image(image_file_name)
cropped_image = crop(image, crop_y_max_pixel)

template_image = read_image(template_image_file_name)
templates_coordinates = manual_template_coordinates()
position_coordinates, templates = multiple_templates_positions(templates_coordinates, cropped_image, template_image)
output_positions(image_file_name, position_coordinates, start_time)

ax.imshow(cropped_image)

# rect = plt.Rectangle((2172, 342), 20, 20, edgecolor='r', facecolor='none')
#
# plt.gca().add_patch(rect)

# rect2 = plt.Rectangle((1336, 490), 20, 20, edgecolor='r', facecolor='none')
#
# plt.gca().add_patch(rect2)
#
# rect3 = plt.Rectangle((2172, 342), 20, 20, edgecolor='r', facecolor='none')
#
# plt.gca().add_patch(rect3)

# note
color = iter(cm.rainbow(numpy.linspace(0, 1, len(position_coordinates))))

for i, position_coordinate in enumerate(position_coordinates):
    print(position_coordinate, templates[i].shape[0], templates[i].shape[1])

    c = next(color)
    y, x = position_coordinate # swapped
    template_rect = plt.Rectangle((x, y),
                                  templates[i].shape[1],
                                  templates[i].shape[0],
                                  edgecolor=c,
                                  facecolor='none')
    plt.gca().add_patch(template_rect)


plt.show()



def test_image_read():
    # x, y, d = image.shape
    # print(x, y)
    #
    # template = crop_template_from_image(image, templates_coordinates[2][0], templates_coordinates[2][1])
    #
    # plt.imshow(template)
    # plt.show()
    #
    # plt.imshow(image)
    plt.imshow(image[0:900, 0:image.shape[1]]) #this crop works
    plt.show()

    return

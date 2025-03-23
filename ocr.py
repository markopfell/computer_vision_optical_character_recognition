import skimage
import pytest
from matplotlib import pyplot as plt

image_file_name = "/Users/mark/computer_vision_optical_character_recognition/source/Sample 1_page1.png"
template_image_file_name = "/Users/mark/computer_vision_optical_character_recognition/source/one.jpeg"

image = skimage.io.imread(image_file_name)

#one
# reading from matplotlib x and y are flipped:
# UL (x, ) to UR (x, ) = ymin to ymax
# UR ( ,y) to LR ( ,y) = xmin to xmax
xmin, ymin = (690, 90)
xmax, ymax = (720, 115)

template_image = image[xmin:xmax, ymin:ymax]

def test_image_read():
    x, y, d = image.shape
    print(x, y)
    plt.imshow(template_image)
    plt.show()

    plt.imshow(image)
    plt.show()

    return


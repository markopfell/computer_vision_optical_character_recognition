import skimage
import os.path
from matplotlib import pyplot as plt

image_file_name = "/Users/mark/computer_vision_optical_character_recognition/source/Sample 1_page1.jpeg"

print(os.path.isfile(image_file_name))

image = skimage.io.imread(image_file_name)
plt.imshow(image)
plt.show()

def read_truth_image():
    return


import skimage as ski
import matplotlib

image = ski.data.coins()
# ... or any other NumPy array!
edges = ski.filters.sobel(image)
ski.io.imshow(edges)
ski.io.show()


def read_truth_image():
    return


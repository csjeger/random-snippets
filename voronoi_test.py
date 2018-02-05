import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
# import matplotlib.image as mpimg
# from PIL import Image
import random


def turn_on_random_pixels(rgbArray, pixelCount):
    for i in range(1, pixelCount):
        x = random.randint(1, rgbArray.shape[0])
        y = random.randint(1, rgbArray.shape[1])
        rgbArray[x, y, 0] = 255
        rgbArray[x, y, 1] = 255
        rgbArray[x, y, 2] = 255
    return rgbArray


def generate_random_points(pixelCount):
    pointList = []
    for i in range(1, pixelCount):
        x = random.randint(1, 512)
        y = random.randint(1, 512)
        pointList.append([x, y])
    return pointList


points = generate_random_points(7)
vor = Voronoi(points)
voronoi_plot_2d(vor)
plt.show()

from skimage import data, io, filter
from skimage.transform import resize
from scipy.misc import imshow
from path import Path
import numpy as np
dir = Path("/home/vasu/Pictures/great_depression/")
side = int(raw_input("Enter size: "))
values = {}
images = dir.files()
i = 0
or_pic = io.imread("MigrantMother.jpg", as_grey=True)
length = or_pic.shape[0] - or_pic.shape[0] % side
width = or_pic.shape[1] - or_pic.shape[1] % side
matrix = np.zeros((length, width))
print matrix.shape
for image in images:
    total = 0.0
    pic = io.imread(image, as_grey=True)
    if pic.max() > 1.0:
        pic = np.divide(pic, 255.0)
    size = min(pic.shape[0], pic.shape[1])
    pic = pic[:size, :size]
    pic = resize(pic, (side, side))
    average = np.mean(pic)
    values[image] = average, pic
for i in range(length / side):
    for j in range(width / side):
        least = 9999
        print side * i, side * (i + 1)
        print side * j, side * (j + 1)
        im = or_pic[side * i: side * (i + 1), side * j: side * (j + 1)]
        mean = np.mean(im)
        for image in values:
            if abs(mean - values[image][0]) < least:
                best_pic, least = values[image][1], abs(mean - values[image][0])
        matrix[side * i: side * (i + 1), side * j: side * (j + 1)] = best_pic
imshow(matrix)

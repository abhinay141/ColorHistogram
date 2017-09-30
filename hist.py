import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('yourImage.jpg')
color=('b', 'g', 'r')
for i, col in enumerate(color):
    histogram2=cv2.calcHist([image], [i], None, [256], [0,256])
    plt.plot(histogram2, color=col)
    plt.xlim([0, 256])
plt.show()




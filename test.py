import cv2
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt

image = cv2.imread("/home/miguff/ÓE/Self-Driving/stop_1.jpeg")
print(type(image))
image = cv2.resize(image, (300, 300))

pyplot.imshow(image)
pyplot.show()
#Centerpont meghatározása
#Bounding box berajzolása
#alakzat meghatározása


import numpy as np
import cv2
import math

# Prints the input image with name(optional)
def show(image,name="image"):
    cv2.imshow(name,image)
    cv2.waitKey(0)
import numpy as np
import cv2
import math
import sys
import Util

# Print full numpy array
np.set_printoptions(threshold=np.nan)

input_img_path="document.png"
input_image = cv2.imread(input_img_path,0)

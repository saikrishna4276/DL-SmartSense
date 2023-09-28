import cv2
import os
import time
import sys

from predict import Classify

filename = "application_data\input_image\input_image.jpg"
        
classifier = Classify(filename)
        # print("B")
result = classifier.recognition()

print(result)
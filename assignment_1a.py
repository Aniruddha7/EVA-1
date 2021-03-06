# -*- coding: utf-8 -*-
"""Assignment 1A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JgE8pTwmnl-PS2hPGqXn1p6aJ76DDWr6
"""

# import the necessary packages
import numpy as np
from urllib.request import urlopen
import cv2
from matplotlib import pyplot as plt

# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# return the image
	return image

image = url_to_image("https://fontsarena-cd5e.kxcdn.com/wp-content/uploads/2019/04/helvetica-now-font-400x364.png")

from google.colab.patches import cv2_imshow
cv2_imshow(image)

edges = cv2.Canny(image,100,200)

cv2_imshow(edges)

#kernel = np.ones((3,3),np.float32)/25
#Vertical edge detector
kernel = np.float32([[-1,0,1],[-1,0,1],[-1,0,1]])

dst = cv2.filter2D(image,-1,kernel)
cv2_imshow(dst)

#Horizontal edge detector

kernel = np.float32([[1,1,1],[0,0,0],[-1,-1,-1]])

dst = cv2.filter2D(image,-1,kernel)
cv2_imshow(dst)

# 45 Degree edge detector
#kernel = np.float32([[-1,0,1],[-2,0,2],[-1,0,1]])
#kernel = np.float32([[0,1,2],[-1,0,1],[-2,-1,0]])
kernel = np.float32([[0,-1,-2],[1,0,-1],[2,1,0]])

dst = cv2.filter2D(image,-1,kernel)
cv2_imshow(dst)

# Blur or Average smoothing
kernel = 1/9*(np.float32([[1,1,1],[1,1,1],[1,1,1]]))

dst = cv2.filter2D(image,-1,kernel)
cv2_imshow(dst)

#Image sharpening
kernel = np.float32([[0,-1,0],[-1,5,-1],[0,-1,0]])

dst = cv2.filter2D(image,-1,kernel)
cv2_imshow(dst)

# Identity function
kernel = np.float32([[0,0,0],[0,1,0],[0,0,0]])

dst = cv2.filter2D(image,-1,kernel)
cv2_imshow(dst)
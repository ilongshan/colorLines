import numpy as np
import os
import cv2
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


radius = 10
rad = radius
xp = []
yp = []
zp = []


with open('../build/output.txt') as f:
	# do something
	number_of_lines = int(f.readline())
	print number_of_lines
	for i in range(number_lines):
		number_of_points = int(f.readline())
		for j in range(number_of_points):
			# do something


# for file in files:
# 	image = cv2.imread( imgDir+file)
# 	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 	for y in xrange(0,gray_image.shape[0]):
# 		for x in xrange(0,gray_image.shape[1]):
# 			if gray_image[y,x] > 0:
# 				theta = x*math.pi/180;
# 				phi = y*math.pi/180;
# 				b = rad*math.sin(phi)*math.cos(theta)
# 				g = rad*math.sin(phi)*math.sin(theta)
# 				r = rad*math.cos(phi)
# 				xp.append(b)
# 				yp.append(g)
# 				zp.append(r)

# 	rad += radius
# 	# print rad


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(xp, yp, zp, c='r', marker='o')

# ax.set_xlabel('B')
# ax.set_ylabel('G')
# ax.set_zlabel('R')

# plt.show()


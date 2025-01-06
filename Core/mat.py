""" Opencv and numpy library import"""
import cv2 as cv
import numpy as np
import os

#adding path to folder containing data so imread knows where to search
#cv.samples.addSamplesDataSearchPath("C:/Users/Bill/Documents/Personal (sept 3, 2023)/Programming/Learning opencv/Core/Enemies")
#importing data theres an bug with pylint but this works

#bullet: np.ndarray = cv.imread(cv.samples.findFile("BulletKin.png"), flags=cv.IMREAD_COLOR)

#print(bullet.shape)

#print(np.array_equal(bullet[0][0], [239,152,0]))

for root, dir, files in os.walk("Core/Enemies/DUMPsprites", topdown=True):
    print(dir)
    #for dirNames in dir:
     #   cv.samples.addSamplesDataSearchSubDirectory('/Enemies/{s}'.format(s=dirNames))
        #print (dirNames)
    #for root, dir, files in os.walk("Core/Enemies/DUMPsprites/{s}".format(s=dir), topdown=True):





"""
for row in range(bullet.shape[0]):
    for column in range(bullet.shape[1]):
        if np.array_equal(bullet[row][column], [239,152,0]):
            bullet[row][column] = [0,0,0] 

cv.imshow("preview", bullet)
cv.waitKey(0)
"""
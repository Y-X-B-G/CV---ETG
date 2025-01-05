""" Opencv and numpy library import"""
import cv2 as cv
import numpy as np

#adding path to folder containing data
cv.samples.addSamplesDataSearchPath("C:/Users/Bill/Documents/Personal (sept 3, 2023)/Programming/Learning opencv/Core/Enemies")
#importing data theres an bug with pylint but this works
bullet = cv.imread(cv.samples.findFile("BulletKin.png"), flags=cv.IMREAD_COLOR)

print(bullet[1][1])
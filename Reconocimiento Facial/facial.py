# https://pypi.org/project/opencv-python/
import io
import cv2 
import numpy as np


faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
img=cv2.imread("/Users/jean/Documents/GitHub/Proyectos Personales y Practicas/Reconocimiento Facial/2.jpg")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("image",img)
cv2.waitKey(0)


cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyWindow()


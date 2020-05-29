import cv2
import numpy as np

img = cv2.imread("lena15.jpg")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # серый
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0) #размытие
imgCanny = cv2.Canny(img, 150, 200) #очертания
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)



print(img.shape)
imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]
cv2.imshow("Image", img)
cv2.imshow("Image resize", imgResize)
cv2.imshow("Image cropped", imgCropped)



img = np.zeros((512,512,3), np.uint8)
print(img.shape)
#img[200:300, 100:300] = 255,0,0
cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.line(img,(0,0),(img.shape[1], img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,400),30,(255,255,0),5)
cv2.putText(img, " OPENCV ",(200,100), cv2.FONT_HERSHEY_COMPLEX, 1.5,(0,150,0),1)
cv2.imshow("img", img)



width, height = 250, 350
img = cv2.imread("2.jpg")

pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("image", img)
cv2.imshow("output", imgOutput)

imghor = np.hstack((img, img))
imgver = np.vstack((img, img))
cv2.imshow("Horizontal", imghor)
cv2.imshow("ver", imgver)


imgHVS = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("COLOR_BGR2HSV", imgHVS)



cv2.waitKey(0)

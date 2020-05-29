import cv2
import numpy as np

cap = cv2.VideoCapture(0)

widthImg = 640
heightImg = 480

cap.set(3, widthImg) #установка размера 
cap.set(4, heightImg)
cap.set(10, 150)

def getContours(img):
	biggest = np.array([]) 
	countours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	x, y, w, h = 0, 0, 0, 0
	for cnt in countours:
		area = cv2.contourArea(cnt)
		maxArea = 0
		if area>5000:
			cv2.drawContours(imgCountour, cnt, -1, (255,0,0), 3)
			peri = cv2.arcLength(cnt, True)
			approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
			if area>maxArea and len(approx)==4:
				biggest = approx
				maxArea = area
	return biggest


def preProcessing(img):
	imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	imgBlur = cv2.GaussianBlur(imgGray, (5,5),1)
	imgCanny = cv2.Canny(imgBlur, 200, 200)
	kernel = np.ones((5,5))
	imgDial = cv2.dilate(imgCanny, kernel, iterations = 2)
	imgThres = cv2.erode(imgDial, kernel, iterations = 1)

	return imgThres

while True:
	success, img = cap.read()
	img = cv2.resize(img, (widthImg, heightImg))
	imgCountour = img.copy()
	imgThres = preProcessing(img)
	getContours(imgThres)
	cv2.imshow("stack Images", imgCountour)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cv2.waitKey(0)
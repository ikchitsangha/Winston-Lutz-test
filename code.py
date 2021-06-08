# import the necessary packages
import matplotlib.pyplot as plt
import imutils
import cv2


# load the image, convert it to grayscale, blur it slightly,
# and threshold it
def calcDisp(p1):
	image = cv2.imread(p1,1)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
	# find contours in the thresholded image
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	i=1
	for c in cnts:
		# compute the center of the contour
		M = cv2.moments(c)
		print('this is i  ',i)
		print(M,c)
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
		i=i+i
		# draw the contour and center of the shape on the image
		cv2.drawContours(image, [c], -1, (56, 23,222), 1)
		cv2.circle(image, (cX, cY), 2, (56, 23,222), -1)
		#cv2.putText(image, "center", (cX - 20, cY - 20),
		#	cv2.FONT_HERSHEY_SIMPLEX, 0.5, (56, 23,222), 2)


	(h, w) = image.shape[:2] #w:image-width and h:image-height
	cv2.circle(image, (w//2, h//2), 2, (56, 23,222), -1) 
	
	
	
	#calculating the displacement
	disx= cX-(w/2)
	disY= (h/2)-cY
	print(f"U displacement= {disx} and V displacement = {disY}")
#	cv2.imshow("display",image)
#	cv2.waitKey(0) 
#	cv2.destroyAllWindows()
	return disx,disY
#opening files
print("enter name of four picutres in gantry positions 0,90,180,270 respectively")
listG=[0,90,180,270]
text1= open("dx.txt",mode='a')
text2= open("dy.txt",mode='a')
listx=[]

for i in range(0,4):
	picIn=input(">> ")
	dX,dY =calcDisp(picIn) # calling the function again and again
	listx.append(dX)
	text1.write(f"{dX},{listG[i]}\n")
	text2.write(f"{dY},{listG[i]}\n")
	
print(f"corrections \n lateral = {listx[0]*.16} mm \n vertical = {listx[1]*.16} mm \n longitudal = {dY*.16} mm") 
cv2.waitKey(0) 
cv2.destroyAllWindows()
	

	

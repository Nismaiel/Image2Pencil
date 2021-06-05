import cv2

img_location = 'C:/Users/NADER ABD EL HADY/Desktop/'
file_name ='aa.jpg'

img = cv2.imread(img_location+file_name)

gray_image= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

invertedGrayImg= 255-gray_image
blurred= cv2.GaussianBlur(invertedGrayImg, (21,21), 0)
invertedBlurImg= 255-blurred

pencil=cv2.divide(gray_image, invertedBlurImg, scale=256.0)

cv2.imshow('original image', img)
cv2.imshow('new image', pencil)
cv2.waitKey(0)
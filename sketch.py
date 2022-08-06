import cv2
img = cv2.imread('suzi.png')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
inverted = 255-gray_img
blur = cv2.GaussianBlur(inverted,(51,51),0)
invertedblur=255-blur
sketch = cv2.divide(gray_img,invertedblur,scale=256)
cv2.imwrite('sketch_image-2.png', sketch)
cv2.imshow('Image',sketch)

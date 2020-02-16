from PIL import Image
import numpy as np
import cv2
import os

image = 'Screenshot_1.png'


img = cv2.imread(image, 0)
test_image = cv2.copyMakeBorder(
    img, 50, 50, 50, 50, borderType=cv2.BORDER_CONSTANT, value=255) #change canvas size

img = test_image

method = cv2.TM_CCOEFF_NORMED
font = cv2.FONT_HERSHEY_SIMPLEX 
arr = []

for i in os.listdir('templates/'): # tamlates into templates folder
    print i
    template = cv2.imread('templates/' + i, 0) # name of the template in ascii code (decimal) 101.png
    w, h = template.shape[::-1]


    res = cv2.matchTemplate(img, template, method)
    threshold = 0.93 # change the accuracy of substitution
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), 255, -1) # -1 is border (full rectangle), 255 is white
        arr.append((i,(pt[0], pt[1])))
        #cv2.putText(img, chr(int(i.split('.')[0])), (pt[0] + 5, pt[1] + 5), font,1, 0, 1, cv2.LINE_AA)


new_image = img.copy()
for i,val in arr:
    cv2.putText(new_image, chr(int(i.split('.')[0])), val, font,
                0.5, 0, 1, cv2.LINE_AA)

Image.fromarray(new_image).show()

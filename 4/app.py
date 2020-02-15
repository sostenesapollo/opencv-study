import cv2
import numpy as np

img = cv2.imread('../watch.jpg', cv2.IMREAD_COLOR)

# color of image pixel
# pixel = img[55,55]

pixel = img[55,55]

# Change pixel color
img[55,55] = [255,255,255]
print(pixel)

# Region Of Image
# roi = img[100:150,100:150]

# Copy and past roi's
img[100:150,100:150] = img[50:100,50:100]
cv2.imshow('Clock',img)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Draw forms and things and put some text
import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)
# bgr
# Draw Line
cv2.line(img, (0,0), (150,450), (255,255,255), 15)

# Draw Rectangle
#             img - start  -   end   -  color   - width 
cv2.rectangle(img, (200,50), (355,200), (0,0,255), 5)

# Draw Circle
#                center- radious- color  - fill
cv2.circle(img, (100,100), 55 , (0,0,255), 1)

# Draw Circle
cv2.circle(img, (500,500), 55 , (0,0,255), -1)

# POLIGONS
points = np.array([[10,5],[500,50],[400,60],[100,200]], np.int32)
# points = points.reshape((-1,1,2))
cv2.polylines(img, [points], True, (0,255,255), 3)

# WRITE
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCv Tuts!!',(100,100), font, 2, (255,255,255))


cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
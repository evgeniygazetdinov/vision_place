import numpy as np
import cv2

img = cv2.imread('1.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0, 0), (200, 200), (255, 255, 255), 15)
cv2.rectangle(img, (15, 15), (200, 150), 5)
cv2.circle(img, (100, 63), 55, (0, 0, 255), -1)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]],  np.int32)
pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX            # font lenght/ color
cv2.putText(img, 'My text', (0, 130), font, 1 ,(200,255,255), 2, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

image = np.ones((512, 512, 3), np.uint8)
#Let's define for points
pts = np.array([[1, 509], [254, 1], [509, 509]], np.int32)
#Let's nw reshape our pints in form requred by polylines
pts = pts.reshape((-1, 1, 2))
cv2.polylines(image, [pts], True, (0, 0, 255), 3)
cv2.rectangle(image, (127, 255), (381, 509), (0, 255, 0), -3)
cv2.circle(image, (254, 382), (127), (255, 0, 0), -4)
cv2.putText(image, 'Noushad Khan', (134, 389), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3)
cv2.imshow('Excercise', image)
cv2.waitKey()
cv2.destroyAllWindows()

import cv2
image = cv2.imread("yo.jpg")
window_name = "image"
cv2.imshow(window_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows()
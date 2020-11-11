import cv2

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

src1 = cv2.imread(".\\lab_camshift\\jackmonkey.jpg")
# cv2.imshow("Jack and monkey Jack", src1)
viewImage(src1, "Jack and monkey Jack")
#grey_img = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)

#bw_img = cv2.threshold(grey_img, 127, 255, 0)
#cv2.imshow("Image", bw_img)
#viewImage(threshold_image, "Чёрно-белый пёсик")
cv2.waitKey(0)
cv2.destroyAllWindows()
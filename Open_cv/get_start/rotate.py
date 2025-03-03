import cv2

image = cv2.imread('D:\Test_Lab\Open_cv\photos\sample1.jpg')

rotate_image = cv2.rotate(image, cv2.ROTATE_180)

cv2.imshow('origin', image)
cv2.imshow('rotate', rotate_image)
cv2.imwrite('D:\\Test_Lab\\Open_cv\\photos\\sample1_rotated.jpg', rotate_image) #save
cv2.waitKey(0)
cv2.destroyAllWindows()
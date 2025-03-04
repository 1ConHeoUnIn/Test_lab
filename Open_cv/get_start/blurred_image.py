import cv2

# Đọc hình ảnh từ file
image = cv2.imread('D:\Test_Lab\Open_cv\photos\duck.jpg')

# Kiểm tra xem hình ảnh có được đọc thành công không
if image is None:
    print("Error: Can not read the image. Pls check your URL.")
else:
    # Hiển thị hình ảnh
    cv2.imshow('Image', image)
    

    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imshow('blurred_image', blurred_image)


    # Chờ người dùng nhấn phím và đóng cửa sổ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
import cv2

# Đọc hình ảnh từ file
image = cv2.imread('D:\Test_Lab\Open_cv\photos\gumble.jpg')

# Kiểm tra xem hình ảnh có được đọc thành công không
if image is None:
    print("Error: Can not read the image. Pls check your URL.")
else:
    # Hiển thị hình ảnh
    cv2.imshow('Image', image)
    

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayscale_image', grayscale_image)

    # Chờ người dùng nhấn phím và đóng cửa sổ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
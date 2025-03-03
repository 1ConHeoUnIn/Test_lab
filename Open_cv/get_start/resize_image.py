import cv2

# Đọc hình ảnh từ file
image = cv2.imread('D:\Test_Lab\Open_cv\photos\hoa.jpg')

# Kiểm tra xem hình ảnh có được đọc thành công không
if image is None:
    print("Error: Can not read the image. Pls check your URL.")
else:
    # Hiển thị hình ảnh
    cv2.imshow('Image', image)
    
   # Thay đổi kích thước hình ảnh
    resized_image = cv2.resize(image, (1920, 1080))
    
    # Hiển thị hình ảnh đã thay đổi kích thước
    cv2.imshow('Resized Image', resized_image)

    # Chờ người dùng nhấn phím và đóng cửa sổ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
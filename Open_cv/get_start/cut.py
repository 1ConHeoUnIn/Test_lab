import cv2

# Đọc hình ảnh từ file
image = cv2.imread('D:\Test_Lab\Open_cv\photos\duck.jpg')

# Kiểm tra kích thước của ảnh gốc
height, width, channels = image.shape
# Kiểm tra xem hình ảnh có được đọc thành công không
if image is None:
    print("Error: Can not read the image. Pls check your URL.")
else:
    # Hiển thị hình ảnh
    cv2.imshow('Image', image)
    print(height, width, channels)

#tọa độ ảnh 
    x1, y1 = 50, 50 
    x2, y2 = 500, 500

    if x1 >= 0 and x2 <= width and y1 >= 0 and y2 <= height:
        # Cắt một phần của ảnh
        cropped_image = image[y1:y2, x1:x2]

        # Hiển thị ảnh cắt
        cv2.imshow('Cropped Image', cropped_image)

    # Chờ người dùng nhấn phím và đóng cửa sổ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
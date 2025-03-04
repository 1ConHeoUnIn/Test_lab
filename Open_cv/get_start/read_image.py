# read image
import cv2

# Đường dẫn đến hình ảnh
image_path = r'D:\Test_Lab\Open_cv\photos\hoa.jpg'  # Sử dụng r'' để tránh lỗi escape

# Đọc hình ảnh từ file
image = cv2.imread(image_path)

# Kiểm tra xem hình ảnh có được đọc thành công không
if image is None:
    print("Error: Không thể đọc hình ảnh. Vui lòng kiểm tra đường dẫn.")
else:
    # Hiển thị hình ảnh
    cv2.imshow('Image', image)

    # Chờ người dùng nhấn phím và đóng cửa sổ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
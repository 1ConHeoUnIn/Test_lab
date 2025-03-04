import cv2

# Đọc hình ảnh từ file
image = cv2.imread('D:\Test_Lab\Open_cv\photos\snow.jpg')

# Kiểm tra xem hình ảnh có được đọc thành công không
if image is None:
    print("Error: Can not read the image. Pls check your URL.")
else:
    # Hiển thị hình ảnh
    cv2.imshow('Image', image)
    

# Thêm văn bản vào ảnh
    text = 'hello'
    position = (200, 150)  # Vị trí văn bản (tọa độ x, y)
    font = cv2.FONT_HERSHEY_SIMPLEX  # Phông chữ
    font_scale = 5  # Kích thước phông chữ
    color = (100, 255, 0)  # Màu văn bản (B, G, R)
    thickness = 3  # Độ dày của văn bản
    line_type = cv2.LINE_AA  # Kiểu đường kẻ

    cv2.putText(image, text, position, font, font_scale, color, thickness, line_type)

    # Hiển thị ảnh đã thêm văn bản
    cv2.imshow('Image with Text', image)


    # Chờ người dùng nhấn phím và đóng cửa sổ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
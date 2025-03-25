import cv2
import pytesseract

# Đường dẫn đến tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Đường dẫn đến hình ảnh
image_path = r'D:\Test_Lab\Open_cv\photos\sample1.jpg'  # Sử dụng r'' để tránh lỗi escape

# Đọc hình ảnh từ file
image = cv2.imread(image_path)

# Kiểm tra xem hình ảnh có được đọc thành công không
if image is None:
    print("Error: Không thể đọc hình ảnh. Vui lòng kiểm tra đường dẫn.")
else:
    # Chuyển đổi sang ảnh xám
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Kiểm tra kích thước
    height, width = image_gray.shape
    print("width : ", width)
    print("height : ", height)

    # Xác định vùng cắt
    x1, y1 = 0, 0 
    x2, y2 = int(width * 0.3), int(height * 0.2)

    # Đảm bảo các chỉ số cắt hợp lệ
    if x1 >= 0 and x2 <= width and y1 >= 0 and y2 <= height:
        # Cắt một phần của ảnh
        cropped_image = image_gray[y1:y2, x1:x2]

        # Điều chỉnh độ tương phản bằng cách sử dụng Histogram Equalization
        equalized_image = cv2.equalizeHist(cropped_image)

        # Áp dụng ngưỡng Otsu
        _, binary_image = cv2.threshold(equalized_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Nhận diện văn bản từ hình ảnh đã cắt
        text = pytesseract.image_to_string(binary_image, lang='vie')
        print("Văn bản nhận diện được:")
        print(text)

        # Hiển thị hình ảnh
        cv2.imshow('Original Image', image_gray)
        cv2.imshow('Cropped Image', cropped_image)
        cv2.imshow('Equalized Image', equalized_image)
        cv2.imshow('Binary Image', binary_image)

        # Chờ người dùng nhấn phím và đóng cửa sổ
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Vùng cắt không hợp lệ.")
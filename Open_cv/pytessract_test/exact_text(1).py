import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Đường dẫn đến hình ảnh
image_path = r'D:\Test_Lab\Open_cv\photos\sample1.jpg'  # Đường dẫn đến ảnh

# Đọc hình ảnh từ file
image = cv2.imread(image_path)
if image is None:
    print("Error: Không thể đọc hình ảnh. Vui lòng kiểm tra đường dẫn.")
else:
    # Chuyển đổi sang ảnh xám
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Làm mịn ảnh (có thể sử dụng Gaussian Blur)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # Ngưỡng hóa ảnh (có thể sử dụng ngưỡng Otsu)
    _, thresh_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Trích xuất văn bản từ ảnh đã xử lý
    custom_config = r'--oem 3 --psm 6 -l vie'  # Cấu hình cho Tesseract
    text = pytesseract.image_to_string(thresh_image, config=custom_config)

    # Hiển thị hình ảnh đã xử lý
    cv2.imshow('Processed Image', thresh_image)
    print(text)

    # Hiển thị hình ảnh gốc
    cv2.imshow('Original Image', image)

    # Chờ người dùng nhấn phím và đóng cửa sổ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
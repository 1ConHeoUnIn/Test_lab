import cv2
import pytesseract

# Đường dẫn đến tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = r'D:\Test_Lab\Open_cv\photos\sample1.jpg'

# Đọc ảnh
image = cv2.imread(image_path)

# Kiểm tra xem hình ảnh có được đọc thành công không
if image is None:
    print("Error: Can not read the image. Pls check your URL.")
else:
    # Chuyển đổi sang ảnh xám
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Làm mịn ảnh
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Ngưỡng hóa (Thresholding)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Cắt ảnh nếu cần (ví dụ: cắt khu vực chứa văn bản)
    # thresh = thresh[y:y+h, x:x+w]  # Thay y, h, x, w bằng giá trị thực tế

    # Hiển thị ảnh đã xử lý
    cv2.imshow('Processed Image', thresh)

    # Trích xuất văn bản
    custom_config = r'--oem 3 --psm 6 -l vie'  # Thay đổi PSM nếu cần
    text = pytesseract.image_to_string(thresh, config=custom_config)
    print(text)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
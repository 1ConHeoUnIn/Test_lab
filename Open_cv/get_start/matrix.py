import cv2
import pytesseract

# Đường dẫn đến tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Đường dẫn đến bức ảnh
image_path = r'D:\Test_Lab\Open_cv\photos\sample1.jpg'

# Đọc bức ảnh
image = cv2.imread(image_path)

# Kiểm tra xem bức ảnh có được đọc thành công hay không
if image is None:
 print("Không thể đọc bức ảnh. Vui lòng kiểm tra đường dẫn.")
else:
   
    # Xuất ra ma trận của bức ảnh
    print("Ma trận của bức ảnh:")
    print(image)
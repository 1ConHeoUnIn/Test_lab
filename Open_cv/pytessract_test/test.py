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

    # Hiển thị ảnh
    cv2.imshow('Original Image', image)

    # Trích xuất văn bản
    text = pytesseract.image_to_string(image, lang='vie')
    print(text)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
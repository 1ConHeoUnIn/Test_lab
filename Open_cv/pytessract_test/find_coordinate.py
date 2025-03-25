import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Đường dẫn đến hình ảnh
image_path = r'D:\Test_Lab\Open_cv\photos\sample1.jpg'  # Sử dụng r'' để tránh lỗi escape

# Đọc hình ảnh từ file
image = cv2.imread(image_path)
if image is None:
    print("Error: Không thể đọc hình ảnh. Vui lòng kiểm tra đường dẫn.")
else:
    # Chuyển đổi sang ảnh xám
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Kiểm tra kích thước
    height, width = image.shape
    print("width : ", width)
    print("height : ", height)
    #
    #threshold_value = 150 # Thay đổi giá trị này để điều chỉnh độ tương phản
    #_, image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # Hàm để cắt và trích xuất văn bản từ ảnh
    def extract_text_from_image(image, x1, y1, x2, y2, should_crop=True):
        if x1 >= 0 and x2 <= image.shape[1] and y1 >= 0 and y2 <= image.shape[0]:
            # Vẽ hình chữ nhật màu tím lên ảnh
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 255), 2)  # Màu tím
            
            if should_crop:
                # Trích xuất văn bản từ vùng đã chỉ định
                cropped_image = image[y1:y2, x1:x2]
                text = pytesseract.image_to_string(cropped_image, lang='vie')
                return text, image
            else:
                return None, image  # Nếu không crop, chỉ trả về ảnh
        else:
            return "Tọa độ không hợp lệ.", None
    # Xác định tọa độ cắt 2
    x1, y1 = int(width*0.25), 0 
    x2, y2 = int(width * 0.75), int(height * 0.25)

    # Gọi hàm để cắt và trích xuất văn bản
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 2', cropped_image)
    print(text)


    

    # Hiển thị hình ảnh
    cv2.imshow('Image', image)
 

    # Chờ người dùng nhấn phím và đóng cửa sổ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
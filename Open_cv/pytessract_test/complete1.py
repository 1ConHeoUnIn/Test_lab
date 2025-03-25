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

    # Hàm để vẽ hình chữ nhật
    def draw_rectangle(image, x1, y1, x2, y2):
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Vẽ hình chữ nhật màu xanh lá

    # Hàm để cắt và trích xuất văn bản từ ảnh
    def extract_text_from_image(image, x1, y1, x2, y2):
        if x1 >= 0 and x2 <= width and y1 >= 0 and y2 <= height:
            # Cắt một phần của ảnh
            cropped_image = image[y1:y2, x1:x2]
            # Trích xuất văn bản từ ảnh đã cắt
            text = pytesseract.image_to_string(cropped_image, lang='vie')
            return text, cropped_image
        else:
            return "Tọa độ không hợp lệ.", None

    # Xác định tọa độ cắt 1
    x1, y1 = 0, 0 
    x2, y2 = int(width * 0.3), int(height * 0.25)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 1', cropped_image)
    print(text)

    # Xác định tọa độ cắt 2
    x1, y1 = int(width * 0.25), 0 
    x2, y2 = int(width * 0.75), int(height * 0.25)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 2', cropped_image)
    print(text)

    # Xác định tọa độ cắt 3
    x1, y1 = int(width * 0.73), 0 
    x2, y2 = width, int(height * 0.18)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 3', cropped_image)
    print(text)

    # Xác định tọa độ cắt 4
    x1, y1 = int(width * 0.07), int(height * 0.25)
    x2, y2 = width, int(height * 0.29)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 4', cropped_image)
    print(text)

     # Xác định tọa độ cắt 5
    x1, y1 = int(width * 0.07), int(height * 0.25)
    x2, y2 = width, int(height * 0.35)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 5', cropped_image)
    print(text)

      # Xác định tọa độ cắt 6
    x1, y1 = int(width * 0.07), int(height * 0.35)
    x2, y2 = width, int(height * 0.38)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 6', cropped_image)
    print(text)

    # Xác định tọa độ cắt 7
    x1, y1 = int(width * 0.07), int(height * 0.38)
    x2, y2 = int(width * 0.5), int(height * 0.42)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 6', cropped_image)
    print(text)

    # Xác định tọa độ cắt 8
    x1, y1 = int(width * 0.5), int(height * 0.38)
    x2, y2 = width, int(height * 0.43)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 8', cropped_image)
    print(text)

    # Xác định tọa độ cắt 9
    x1, y1 = int(width * 0.07), int(height * 0.43)
    x2, y2 = width, int(height * 0.46)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 9', cropped_image)
    print(text)

     # Xác định tọa độ cắt 10
    x1, y1 = int(width * 0.07), int(height * 0.46)
    x2, y2 = width, int(height * 0.5)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 10', cropped_image)
    print(text)

      # Xác định tọa độ cắt 11
    x1, y1 = int(width * 0.07), int(height * 0.5)
    x2, y2 = width, int(height * 0.53)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 11', cropped_image)
    print(text)

    # Xác định tọa độ cắt 12
    x1, y1 = int(width * 0.07), int(height * 0.53)
    x2, y2 = width, int(height * 0.56)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 12', cropped_image)
    print(text)

     # Xác định tọa độ cắt 13
    x1, y1 = int(width * 0.07), int(height * 0.56)
    x2, y2 = width, int(height * 0.6)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 13', cropped_image)
    print(text)

    # Xác định tọa độ cắt 14
    x1, y1 = int(width * 0.07), int(height * 0.6)
    x2, y2 = width, int(height * 0.63)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 14', cropped_image)
    print(text)

     # Xác định tọa độ cắt 15
    x1, y1 = int(width * 0.07), int(height * 0.63)
    x2, y2 = width, int(height * 0.69)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 15', cropped_image)
    print(text)

    # Hiển thị hình ảnh
    cv2.imshow('Image', image)

     # Xác định tọa độ cắt 16
    x1, y1 = int(width * 0.02), int(height * 0.7)
    x2, y2 = int(width * 0.3), int(height * 0.77)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 16', cropped_image)
    print(text)

    # Hiển thị hình ảnh
    cv2.imshow('Image', image)

      # Xác định tọa độ cắt 17
    x1, y1 = int(width * 0.31), int(height * 0.7)
    x2, y2 = int(width * 0.57), int(height * 0.77)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 17', cropped_image)
    print(text)

       # Xác định tọa độ cắt 18
    x1, y1 = int(width * 0.57), int(height * 0.7)
    x2, y2 = int(width * 1), int(height * 0.77)
    draw_rectangle(image, x1, y1, x2, y2)  # Vẽ hình chữ nhật
    text, cropped_image = extract_text_from_image(image, x1, y1, x2, y2)
    cv2.imshow('Cropped 18', cropped_image)
    print(text)

    # Hiển thị hình ảnh
    cv2.imshow('Image', image)

    # Chờ người dùng nhấn phím và đóng cửa sổ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
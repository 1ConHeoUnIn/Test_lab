# read image
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Đường dẫn đến hình ảnh
image_path = r'D:\Test_Lab\Open_cv\photos\sample2.jpg'  # Sử dụng r'' để tránh lỗi escape

# Đọc hình ảnh từ file
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
boxes = pytesseract.image_to_boxes(image, lang='vie')

height,weight = image.shape
print("height : ", h)
print("width : ", w)

x1, y1 =  0, 0 
x2, y2 = 180, h//5

if x1 >= 0 and x2 <= width and y1 >= 0 and y2 <= height:
    # Cắt một phần của ảnh
    croped_image = image[y1:y2, x1:x2]
text = pytesseract.image_to_string(croped_image, lang='vie')

# Kiểm tra xem hình ảnh có được đọc thành công không
if image is None:
    print("Error: Không thể đọc hình ảnh. Vui lòng kiểm tra đường dẫn.")
else:
    # Hiển thị hình ảnh
    cv2.imshow('Image', image)
    cv2.imshow('Croped_Image', croped_image)

    for b in boxes.splitlines():
        b = b.split(' ')
       #     print(b)
        x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
        cv2.rectangle(image,(x,height-y),(w,height-h),(0,55,255),2) #cv2.rectangle(image, start_point, end_point, color, thickness)

    print(text)

    # Chờ người dùng nhấn phím và đóng cửa sổ
    cv2.waitKey(0)
    cv2.destroyAllWindows()


import cv2
import pytesseract

# Đường dẫn đến tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = r'D:\Test_Lab\Open_cv\photos\sample3.jpg'

# Đọc ảnh
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
height, width = image.shape
boxes = pytesseract.image_to_boxes(image, lang='vie')
#image = cv2.resize(image, (height*2, width*2))


# Kiểm tra xem hình ảnh có được đọc thành công không
if image is None:
    print("Error: Can not read the image. Pls check your URL.")
else:

    
    print(boxes)
   

    # Trích xuất văn bản
  
    for b in boxes.splitlines():
        b = b.split(' ')
       #     print(b)
        x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
        cv2.rectangle(image,(x,height-y),(w,height-h),(0,55,255),2) #cv2.rectangle(image, start_point, end_point, color, thickness)
           
# Hiển thị ảnh
    cv2.imshow('grayscale_image', image)
    text = pytesseract.image_to_string(image, lang='vie')
    print(text)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
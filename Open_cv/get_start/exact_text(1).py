import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = r'D:\Test_Lab\Open_cv\photos\sample1.jpg'
image = cv2.imread(image_path)
# Kiểm tra kích thước của ảnh gốc
height, width, channels = image.shape
# Kiểm tra xem hình ảnh có được đọc thành công không
if image is None:
    print("Error: Can not read the image. Pls check your URL.")
else:
 
     print('height = ', height, 'width = ', width, 'channels = ', channels)

     
w=width//2
h=height//2
resized_image = cv2.resize(image, (w,h)) #width ,height  #thu nhỏ cho ảnh rõ hơn
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY) #đổi sang màu xám cho dễ nhận dạng
cv2.imshow('Image', image) 
cv2.imshow('resized_image',resized_image)
cv2.imshow('gray_image',gray_image)

text = pytesseract.image_to_string(gray_image, lang='vie')
print(text)

cv2.waitKey(0)
cv2.destroyAllWindows()




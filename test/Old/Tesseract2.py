import cv2
import pytesseract
import os

# ระบุพาธไปยังไดเรกทอรีที่เก็บภาพ
images_path = './test/images/'

# ดึงรายการไฟล์ทั้งหมดในไดเรกทอรี
files = os.listdir(images_path)

# ลูปผ่านแต่ละไฟล์ในไดเรกทอรี
for file in files:
    # สร้างพาธไฟล์เต็ม
    file_path = os.path.join(images_path, file)
    
    # ตรวจสอบว่าไฟล์เป็นภาพหรือไม่
    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        # โหลดภาพ
        image = cv2.imread(file_path)

        # แปลงภาพเป็นสีเทา
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # แปลงภาพเป็นภาพสองสี (binary image)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

        # ทำการขยายภาพเพื่อทำให้ตัวอักษรหนาขึ้น
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
        dilated = cv2.dilate(thresh, kernel, iterations=1)

        # ใช้การเบลอแบบ median เพื่อกำจัด noise
        denoised = cv2.medianBlur(dilated, 1)

        # ใช้ Tesseract เพื่อดึงข้อความจากภาพพร้อมการตั้งค่าที่กำหนด
        config = r'--oem 3 --psm 12 -l eng'
        text = pytesseract.image_to_string(denoised, config=config)

        # พิมพ์ข้อความที่ดึงออกมาได้
        print(f"Extracted Text from {file}:")
        print(text.split("\n"))
        print("\n" + "-"*50 + "\n")

import re
from PIL import Image
import pytesseract

# ตั้งค่าเส้นทางของ tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def find_dates(text):
    # สร้าง regex pattern ที่จะตรวจสอบตัวเลขหรือตัวอักษรที่ติดกัน
    pattern = rf'[a-zA-Z0-9]{{{5}}}'
    # ใช้ re.findall เพื่อตรวจสอบว่าในข้อความมีชุดที่ตรงกับ pattern หรือไม่
    matches = re.findall(pattern, text)

    # สร้าง regex pattern สำหรับวันที่รูปแบบ dd/mm/yy หรือ dd-mm-yyyy
    # ตัวอย่างนี้รองรับทั้งวันที่ในรูปแบบ 2 หลัก และ 4 หลัก
    date_pattern = r'\b(?:0[1-9]|[12][0-9]|3[01])[-/](?:0[1-9]|1[0-2])[-/](?:\d{2}|\d{4})\b'
    
    # ใช้ re.findall เพื่อตรวจสอบว่าในข้อความมีชุดที่ตรงกับ pattern หรือไม่
    dates = re.findall(date_pattern, text)
    return (matches, dates)

# โหลดภาพ
image_path = "./captured_images/230724_034736.jpg"
image = Image.open(image_path)

# ใช้ Tesseract เพื่อดึงข้อความจากภาพ
text = pytesseract.image_to_string(image, lang='eng+tha')

print(find_dates(text))
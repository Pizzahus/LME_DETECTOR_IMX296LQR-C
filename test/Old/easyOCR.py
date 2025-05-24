import easyocr
import os

reader = easyocr.Reader(['en'], gpu=False) # this needs to run only once to load the model into memory
# reader = easyocr.Reader(['ch_sim','en'], gpu=False)

# ระบุพาธไปยังไดเรกทอรีที่เก็บภาพ
images_path = './test/images/'

# ดึงรายการไฟล์ทั้งหมดในไดเรกทอรี
files = os.listdir(images_path)

# ลูปผ่านแต่ละไฟล์ในไดเรกทอรี
for file in files:
    # สร้างพาธไฟล์เต็ม
    file_path = os.path.join(images_path, file)

    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        result = reader.readtext(file_path, detail=0)
        print(result)
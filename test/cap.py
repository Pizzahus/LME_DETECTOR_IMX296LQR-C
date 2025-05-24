from picamera2 import Picamera2
from gpiozero import Button
import cv2
from datetime import datetime
from time import time
import pytesseract
import numpy as np

# ตั้งค่า Tesseract (ปรับเส้นทางตามระบบของคุณ)
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
X1, Y1, X2, Y2 = 230, 180, 800, 450

picam2 = Picamera2()
sensor = Button(23, pull_up=True, bounce_time=0.05)  # ตั้งค่า bounce_time = 0.1 วินาที

config = picam2.create_still_configuration(main={"size": (1024, 768)}, buffer_count=50)
picam2.configure(config)
picam2.start()

# ตั้งค่า Exposure
picam2.set_controls(
    {"AeEnable": False, "ExposureTime": 1000, "AnalogueGain": 8.0}  # ปิด Auto Exposure
)

metadata = picam2.capture_metadata()
print(metadata["ExposureTime"], metadata["AnalogueGain"])

# cv2.namedWindow("IMX296 Preview", cv2.WINDOW_NORMAL)
# print("กด SPACEBAR เพื่อถ่ายภาพและอ่านตัวอักษร, Q เพื่อออก")


def preprocess_for_ocr(image):
    # # แปลงเป็น grayscale
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # # ลบ noise ด้วย Gaussian blur
    # blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # # Adaptive thresholding
    # thresh = cv2.adaptiveThreshold(
    #     blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    # )

    # # Morphological operations เพื่อลบ noise เล็กๆ
    # kernel = np.ones((3, 3), np.uint8)
    # processed = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

    # return processed
    return image


def detect_and_recognize_text(image):
    # Preprocess ภาพ
    processed = preprocess_for_ocr(image)

    # ใช้ Tesseract OCR อ่านข้อความ
    config = r"--oem 1 --psm 6 -c tessedit_char_whitelist=0123456789/"
    text = pytesseract.image_to_string(image, config=config)

    return text, processed


def captured():
    start_time = time()

    still = picam2.capture_array()
    cropped_frame = still[Y1:Y2, X1:X2]
    still_bgr = cv2.cvtColor(still, cv2.COLOR_RGB2BGR)
    inverted_image = cv2.bitwise_not(cropped_frame)

    # ย่อลงครึ่งหนึ่ง (50%)
    scale_percent = 50  # เปอร์เซ็นต์จากขนาดเดิม
    width = int(inverted_image.shape[1] * scale_percent / 100)
    height = int(inverted_image.shape[0] * scale_percent / 100)
    dim = (width, height)

    # ย่อภาพ
    resized_image = cv2.resize(inverted_image, dim, interpolation=cv2.INTER_AREA)

    # ตรวจจับและอ่านข้อความ
    text, processed_img = detect_and_recognize_text(resized_image)

    # แสดงภาพที่ผ่านการประมวลผล
    cv2.imshow("Processed Image", processed_img)

    # พิมพ์ข้อความที่อ่านได้
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y, %H:%M:%S")
    print(timestamp, text.strip())

    # แสดงข้อความบนภาพต้นฉบับ
    if text.strip():
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(
            still_bgr,
            f"Text: {text.strip()}",
            (10, 30),
            font,
            0.7,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )

    cv2.imshow("Captured Image", still_bgr)

    # จับเวลาที่สิ้นสุด
    end_time = time()
    processing_time = end_time - start_time
    print(f"Processing time => {processing_time:.2f}\n")

tiggered = False
count = 0
while True:
    preview = picam2.capture_array()
    preview_bgr = cv2.cvtColor(preview, cv2.COLOR_RGB2BGR)
    cv2.rectangle(preview_bgr, (X1, Y1), (X2, Y2), (0, 0, 255), 2)  # สีแดง (BGR)
    
    cv2.imshow("IMX296 Preview", preview_bgr)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
    elif key == 32:  # spacebar
        captured()
    elif sensor.is_pressed and not tiggered:  # ตรวจสอบสถานะปุ่มแบบ polling
        tiggered = True
        count+=1
        print("Count: ", count)
        captured()
    elif not sensor.is_pressed:  # ตรวจสอบสถานะปุ่มแบบ polling
        tiggered = False
        


picam2.stop()
cv2.destroyAllWindows()

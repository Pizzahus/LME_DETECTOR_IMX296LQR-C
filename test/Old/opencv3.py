import cv2
import os
from ultralytics import YOLO
from datetime import datetime

# โหลดโมเดล YOLO
model = YOLO('./test/model/bestX.pt')

# ตั้งค่าขนาดของภาพและการตรวจจับ
imgsz = 256  # กำหนด imgsz ให้เป็นตัวคูณของ 32
conf_threshold = 0.3  # เกณฑ์ความเชื่อมั่นสำหรับการตรวจจับ
desired_width = 640
desired_height = 480
onLoad = False

# กำหนดชื่อของคลาส
classNames = ["NG", "OK"]

# กำหนดโฟลเดอร์ที่จะเก็บภาพ
output_dir = './test/captured_images'
os.makedirs(output_dir, exist_ok=True)  # สร้างโฟลเดอร์หากยังไม่มี

# เปิดการใช้งานกล้องเว็บแคม
cap = cv2.VideoCapture(0)  # 0 คือกล้องดีฟอลต์

while True:
    ret, frame = cap.read()  # อ่านเฟรมจากกล้อง
    if not ret:
        print("เกิดข้อผิดพลาดในการจับภาพจากกล้องเว็บแคม.")
        break
    
    # แสดงฟีดจากกล้องเว็บแคม
    cv2.imshow('WEBCAM', frame)
    
    # ตรวจสอบการกดปุ่ม
    key = cv2.waitKey(1) & 0xFF
    
    if not onLoad:
        onLoad = True
        resized_frame = cv2.resize(frame, (desired_width, desired_height))
        cv2.imshow('Detection Result', resized_frame)
    
    # ถ้ากดปุ่ม 's'
    if key == ord('s'):
        # ปรับขนาดเฟรมให้เป็นขนาดที่ต้องการ
        resized_frame = cv2.resize(frame, (desired_width, desired_height))
        
        # ใช้โมเดล YOLO เพื่อทำการพยากรณ์
        results = model.predict(source=resized_frame, imgsz=imgsz, conf=conf_threshold)
        
        # แสดงผลลัพธ์การตรวจจับ
        detections = results[0].boxes
        
        for detection in detections:
            conf = detection.conf[0]
            cls = detection.cls[0]
            print(f"ผลลัพธ์: {classNames[int(cls)]}, ความเชื่อมั่น: {conf:.2f}")
        
        # วาดกรอบการตรวจจับบนเฟรม
        annotated_frame = results[0].plot()
        
        # สร้างชื่อไฟล์ที่มีเวลา
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_filename = f'{output_dir}/image_{timestamp}.jpg'
        
        # บันทึกภาพที่จับได้และภาพที่มีการตรวจจับ
        cv2.imwrite(image_filename, annotated_frame)  # บันทึกภาพที่มีการตรวจจับ
        
        # แสดงภาพที่มีการตรวจจับ
        cv2.imshow('Detection Result', annotated_frame)
    
    # ออกจากลูปถ้ากดปุ่ม 'q'
    if key == ord('q'):
        break

# ปิดการใช้งานกล้องและปิดหน้าต่างทั้งหมด
cap.release()
cv2.destroyAllWindows()

import cv2
import os
from ultralytics import YOLO

# โหลดโมเดล
model = YOLO('./test/bestX.pt')

# เส้นทางไปยังโฟลเดอร์ที่เก็บภาพ
image_folder_path = 'C:/Users/pizza/Desktop/YOLO8/test/data'

# ตั้งค่าขนาดของเฟรมที่ต้องการ
desired_width = 640
desired_height = 480
imgsz = 256  # กำหนด imgsz ให้เป็นตัวคูณของ 32

# กำหนดกรอบที่ต้องการตรวจจับ (x1, y1, x2, y2)
x1, y1, x2, y2 = 100, 100, 540, 200

# รับรายชื่อไฟล์ทั้งหมดในโฟลเดอร์
image_files = [f for f in os.listdir(image_folder_path) if f.endswith(('JPG', 'jpeg', 'png', 'bmp'))]

for image_file in image_files:
    image_path = os.path.join(image_folder_path, image_file)
    frame = cv2.imread(image_path)
    
    if frame is None:
        print(f"Error loading image {image_file}")
        continue
    
    # ปรับขนาดเฟรม
    resized_frame = cv2.resize(frame, (desired_width, desired_height))
    
    # ใช้โมเดลเพื่อทำการพยากรณ์
    results = model.predict(source=resized_frame, imgsz=imgsz, conf=0.3)
    
    # แสดงผลลัพธ์ของการตรวจจับ
    detections = results[0].boxes

    classNames = ["NG", "OK"]
    for detection in detections:
        # แสดงค่าทั้งหมดที่ได้รับ
        print("Detection values:")
        conf = detection.conf[0]
        cls = detection.cls[0]
        
        print(f"Result: {classNames[int(cls)]}, Confidence: {conf:.2f}")

    # วาดกรอบการตรวจจับบนเฟรมที่ครอป
    annotated_cropped_frame = results[0].plot()  # ใช้ plot() เพื่อวาดกรอบการตรวจจับบนเฟรมที่ครอป

    # แสดงผลเฟรมที่มีกรอบการตรวจจับ
    cv2.imshow('Image', annotated_cropped_frame)
    
    # รอ 1 วินาที
    cv2.waitKey(1000)

# ปิดการใช้งานและหน้าต่างการแสดงผล
cv2.destroyAllWindows()

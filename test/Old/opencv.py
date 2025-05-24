import cv2
from ultralytics import YOLO

# โหลดโมเดล
model = YOLO('./test/bestX.pt')

# เปิดไฟล์วิดีโอ
# cap = cv2.VideoCapture('./test/data/IMG_9884.MOV')
cap = cv2.VideoCapture(0)

# ตั้งค่าขนาดของเฟรมที่ต้องการ
desired_width = 640
desired_height = 480
imgsz = 256  # กำหนด imgsz ให้เป็นตัวคูณของ 32

# กำหนดกรอบที่ต้องการตรวจจับ (x1, y1, x2, y2)
x1, y1, x2, y2 = 100, 100, 540, 200

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # ปรับขนาดเฟรม
    resized_frame = cv2.resize(frame, (desired_width, desired_height))
    cv2.rectangle(resized_frame, (x1, y1), (x2, y2), (0, 0, 255), 2)  # สีแดง (BGR)
    
    # ครอปเฟรมตามกรอบที่กำหนด
    cropped_frame = resized_frame[y1:y2, x1:x2]
    
    # ใช้โมเดลเพื่อทำการพยากรณ์
    results = model.predict(source=cropped_frame, imgsz=imgsz, conf=0.5)
    
    # วาดกรอบการตรวจจับบนเฟรมที่ครอป
    annotated_cropped_frame = results[0].plot()  # ใช้ plot() เพื่อวาดกรอบการตรวจจับบนเฟรมที่ครอป
    
    # ใส่กรอบที่ครอปกลับเข้าไปในเฟรมที่ขนาดเดิม
    resized_frame[y1:y2, x1:x2] = annotated_cropped_frame
    
    # แสดงผลเฟรมที่มีกรอบการตรวจจับ
    cv2.imshow('Video', resized_frame)
    
    # ออกจากลูปเมื่อกดปุ่ม 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ปิดการใช้งานและหน้าต่างการแสดงผล
cap.release()
cv2.destroyAllWindows()

#!/bin/bash
# === สร้างและเปิดใช้งาน venv ===
python3 -m venv detection_venv
source detection_venv/bin/activate

# === อัปเดต pip และติดตั้งไลบรารีที่จำเป็น ===
pip install --upgrade pip
pip install pyside6 pytesseract pywifi comtypes requests pyserial gpiozero ultralytics numpy opencv-python opencv-contrib-python

echo "ติดตั้งเสร็จสมบูรณ์!"
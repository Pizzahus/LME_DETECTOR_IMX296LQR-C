@echo off
REM === สร้างและเปิดใช้งาน venv ===
python -m venv detection_venv
call detection_venv\Scripts\activate

REM === ติดตั้งไลบรารีที่จำเป็น ===
pip install --upgrade pip
pip install pyside6 pytesseract pywifi comtypes requests pyserial gpiozero ultralytics numpy opencv-python opencv-contrib-python

echo ติดตั้งเสร็จสมบูรณ์!
pause
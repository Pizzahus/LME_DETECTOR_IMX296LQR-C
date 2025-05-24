import serial
import time

ser = serial.Serial(port='COM19', baudrate=9600, timeout=1)

def send_command(command):
    ser.write(command)
    time.sleep(0.1)

# ตั้งค่าตารางรหัสตัวอักษรเป็น TIS-620 (ถ้ารองรับ)
# ESC t n (n = 26 สำหรับ TIS-620)
set_code_page = b'\x1b\x74\x1a'
send_command(set_code_page)
send_command(b'\x1b\x61\x01')
send_command(b'\x1B\x21\x30')
send_command(b'\x1B\x45\x01')

# ข้อความภาษาไทย
thai_text = "สวัสดีครับasdasdsad\n"

# แปลงข้อความเป็น TIS-620
encoded_text = thai_text.encode('tis-620')

# ส่งข้อความภาษาไทยไปยังเครื่องพิมพ์
send_command(encoded_text)

# ตัดกระดาษ
cut_paper = b'\x1d\x56\x42\x00'
send_command(cut_paper)

ser.close()

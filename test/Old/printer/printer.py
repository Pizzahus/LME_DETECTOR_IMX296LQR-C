import serial
import time

ser = serial.Serial(port='COM19', baudrate=9600, timeout=1)

def send_command(command):
    ser.write(command)
    time.sleep(0.1)

# รีเซ็ตเครื่องพิมพ์
send_command(b'\x1b\x40')
# พิมพ์ข้อความ
send_command(b'\x1b\x47\x01')
send_command(b'Hello, ESC/POS Printer!\n')
send_command(b'Hello, ESC/POS Printer!\n')
# จัดข้อความชิดกลาง
send_command(b'\x1b\x61\x00')
# ตัดกระดาษ
send_command(b'\x1d\x56\x42\x00')

ser.close()

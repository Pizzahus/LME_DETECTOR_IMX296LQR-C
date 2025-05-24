import serial
import time

def send_command(command):
    ser.write(command)
    time.sleep(0.1)

# ตั้งค่าพอร์ตอนุกรม
ser = serial.Serial(
    port='COM15',  # หรือ COMx ใน Windows
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)


send_command(b'\x1b\x61\x01')
send_command(b'\x1B\x21\x00')
send_command(b'\x1B\x45\x01')

# พิมพ์โลโก้จากหน่วยความจำ
# FS p n m : n = ID ของโลโก้, m = โหมดการพิมพ์ (0 หรือ 1)
print_logo = b'\x1c\x70\x01\x00'  # ตัวอย่าง ID โลโก้ที่ 1 (โปรดตรวจสอบคู่มือเครื่องพิมพ์)

send_command(print_logo)
send_command(b'\x1b\x61\x01')

set_code_page = b'\x1b\x74\x1a'
send_command(set_code_page)

# พิมพ์ข้อความหลังจากพิมพ์โลโก้
text = "128.42 กรัม\n"
send_command(text.encode('tis-620'))

# ตัดกระดาษหลังพิมพ์เสร็จ
cut_paper = b'\x1d\x56\x42\x00'
send_command(cut_paper)

# ปิดการเชื่อมต่อ
ser.close()

import gpiod
import os
import sys

def read_gpio():
    CHIP = 'gpiochip0'
    LINE_OFFSET = 23
    
    try:
        chip = gpiod.Chip(CHIP)
        line = chip.get_line(LINE_OFFSET)
        line.request(consumer="python-example", type=gpiod.LINE_REQ_DIR_IN)
        value = line.get_value()
        print(f"ค่า GPIO {LINE_OFFSET}: {value}")
    except PermissionError:
        print("พบข้อผิดพลาดด้านสิทธิ์ การแก้ไข:")
        print("1. ใช้คำสั่ง: sudo usermod -a -G gpio $USER")
        print("2. ล็อกอินใหม่หรือรีบูต")
        print("3. หรือรันโปรแกรมด้วย sudo")
        sys.exit(1)
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {str(e)}")
        sys.exit(1)
    finally:
        if 'line' in locals():
            line.release()
        if 'chip' in locals():
            chip.close()

if __name__ == '__main__':
    # ตรวจสอบสิทธิ์ก่อนรัน
    if not os.access('/dev/gpiochip0', os.R_OK|os.W_OK):
        print("คำเตือน: อาจมีปัญหาเรื่องสิทธิ์การเข้าถึง GPIO")
    
    while True:
        read_gpio()
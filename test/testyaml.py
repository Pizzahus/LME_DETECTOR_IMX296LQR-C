from resources.ConfigManager import ConfigManager

# สร้าง instance ของ ConfigManager
config = ConfigManager()

# 1. การใช้งานกับ Hardware
gpio_settings = config.get_gpio_settings()
print(f"Sensor Pin: GPIO{gpio_settings['sensorPin']}")
print(f"Buzzer Pin: GPIO{gpio_settings['buzzerPin']}")

# 2. การตั้งค่ากล้อง
camera_settings = config.get_camera_settings()
if camera_settings['autoFocus']:
    print("โหมดโฟกัสอัตโนมัติเปิดใช้งาน")

# 3. การจัดการเทมเพลต
config.update_template(lot="LOT20230001", mfg="20230115", exp="20240115")

# 4. การจัดการสถิติ
config.update_counter(ok=1)  # เพิ่มสินค้าที่ผ่าน
config.update_counter(ng=1)  # เพิ่มสินค้าไม่ผ่าน

# 5. รีเซ็ตสถิติ
config.reset_counters()
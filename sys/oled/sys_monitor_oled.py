from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont
from gpiozero import Button
import psutil
import netifaces
import subprocess
import time

# ???? toggle ??? GPIO 4
button = Button(4)
show_network = False

# OLED
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

# ?????
font_small = ImageFont.load_default()
font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)

# toggle display
def toggle_display():
    global show_network
    show_network = not show_network

button.when_pressed = toggle_display

def get_temperature():
    try:
        output = subprocess.check_output(["vcgencmd", "measure_temp"]).decode()
        temp_str = output.replace("temp=", "").replace("'C\n", "")
        return float(temp_str)
    except Exception:
        return None

def get_ip(iface):
    try:
        return netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
    except:
        return "N/A"

def get_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq().current
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    temp = get_temperature()
    return cpu_percent, cpu_freq, ram, disk, temp

while True:
    with canvas(device) as draw:
        draw.text((0, 0), "Polipharm Co.,Ltd.", font=font_large, fill=255)

        if show_network:
            draw.text((0, 20), f"eth0: {get_ip('eth0')}", font=font_small, fill=255)
            draw.text((0, 30), f"eth1: {get_ip('eth1')}", font=font_small, fill=255)
            draw.text((0, 40), f"wlan0: {get_ip('wlan0')}", font=font_small, fill=255)
            draw.text((0, 50), "Press to return", font=font_small, fill=255)
        else:
            cpu, freq, ram, disk, temp = get_system_info()
            draw.text((0, 20), f"CPU: {cpu:.1f}% @ {freq:.0f}MHz", font=font_small, fill=255)
            draw.text((0, 30), f"RAM: {ram.used/1024/1024:.2f}/{ram.total//1024//1024}MB", font=font_small, fill=255)
            draw.text((0, 40), f"Disk: {disk.used/1024/1024/1024:.2f}/{disk.total//1024//1024//1024}GB", font=font_small, fill=255)
            if temp is not None:
                draw.text((0, 50), f"Temp: {temp:.1f} C", font=font_small, fill=255)
            else:
                draw.text((0, 50), "Temp: N/A", font=font_small, fill=255)

    time.sleep(0.5)

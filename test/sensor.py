from gpiozero import Button
from datetime import datetime
from time import sleep

sensor = Button(23, pull_up=True, bounce_time=0.05)  # ตั้งค่า bounce_time = 0.1 วินาที

def on_press():
        now = datetime.now()
        timestamp = now.strftime("%d/%m/%Y, %H:%M:%S")
        print(f"{timestamp} => Sensor triggered")

sensor.when_pressed = on_press
while True:
    pass
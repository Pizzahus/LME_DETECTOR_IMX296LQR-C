import asyncio
from bleak import BleakClient

PRINTER_ADDRESS = "XX:XX:XX:XX:XX:XX"  # ใส่ที่อยู่ของเครื่องพิมพ์ Bluetooth LE ของคุณ

async def send_to_printer(address, message: str):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")
        # ส่งข้อความไปยังบริการที่ระบุและ characteristic
        # คุณอาจต้องแก้ไข UUIDs ของบริการและ characteristic
        await client.write_gatt_char("00002a56-0000-1000-8000-00805f9b34fb", message.encode())

loop = asyncio.get_event_loop()
loop.run_until_complete(send_to_printer(PRINTER_ADDRESS, "Hello, world!"))

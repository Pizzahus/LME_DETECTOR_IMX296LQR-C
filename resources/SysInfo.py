import netifaces
import subprocess
import psutil

class SystemMonitor:
    def __init__(self):
        super().__init__()

    def get_temperature(self):
        try:
            output = subprocess.check_output(["vcgencmd", "measure_temp"]).decode()
            temp_str = output.replace("temp=", "").replace("'C\n", "")
            return float(temp_str)
        except Exception:
            return None

    def get_ip(self, iface: str = "eth0"):
        try:
            return netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
        except Exception:
            return "N/A"

    def get_cpu_percent(self):
        try:
            return float(psutil.cpu_percent(interval=None))
        except Exception:
            return 0.0

    def get_cpu_freq(self):
        try:
            freq = psutil.cpu_freq()
            return float(freq.current) if freq else 0.0
        except Exception:
            return 0.0

    def get_ram(self):
        try:
            return psutil.virtual_memory()
        except Exception:
            return None

    def get_disk(self):
        try:
            return psutil.disk_usage('/')
        except Exception:
            return None

    def get_all_info(self):
        return {
            "cpu_percent": self.get_cpu_percent(),
            "cpu_freq": self.get_cpu_freq(),
            "ram": self.get_ram(),
            "disk": self.get_disk(),
            "temperature": self.get_temperature()
        }
import sys
import yaml
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class Counter:
    ok: int
    ng: int


@dataclass
class RectangleSettings:
    X1: int
    Y1: int
    X2: int
    Y2: int


@dataclass
class TemplateLME:
    lot: str
    mfg: str
    exp: str

@dataclass
class SystemSettings:
    ocrEngine: str
    delayShutter: int
    delayBeforeReject: int
    rejectionPeriod: int
    numberStickerBeforeDetection: int
    rotateImage: int
    detectionPercentage: int
    detectionResizeImage: int
    saveImage: bool

@dataclass
class CameraSettings:
    ExposureTime: int
    AnalogueGain: int
    Brightness: int
    Contrast: int
    Saturation: int
    Sharpness: int
    FrameRate: int

@dataclass
class GPIOSettings:
    DI0: int
    BUZZER: int
    LED0: int
    LED1: int
    DI1: int
    DO0: int
    DO1: int
    L0: int
    L1: int


class ConfigManager:
    def __init__(self, config_path: str = 'configuration.yaml'):
        self.config_path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        if not self.config_path.exists():
            print("ไม่พบไฟล์ข้อมูลการตั้งค่า configuration.yaml!")
            sys.exit(1)

        with open(self.config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}

    # บันทึกการตั้งค่า
    def save_config(self, config: Dict[str, Any] = None) -> None:
        with open(self.config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config or self.config, f, sort_keys=False, allow_unicode=True)

    # อ่านข้อมูล lot, mfg, exp
    def get_template(self) -> TemplateLME:
        data = self.config.get('template', {})
        return TemplateLME(
            lot=data.get('lot', ''),
            mfg=data.get('mfg', ''),
            exp=data.get('exp', ''),
        )

    # อ่านข้อมูลกรอบตรวจจับ
    def get_rectangle(self) -> RectangleSettings:
        data = self.config.get('hardware', {}).get('rectangle', {})
        return RectangleSettings(
            X1=data.get('x1', ''),
            X2=data.get('x2', ''),
            Y1=data.get('y1', ''),
            Y2=data.get('y2', ''),
        )

    # อ่านข้อมูลจำนวนชิ้นงาน
    def get_count(self) -> Counter:
        data = self.config.get('counters', {})
        return Counter(
            ok=data.get('ok', 0),
            ng=data.get('ng', 0),
        )

    # อ่านข้อมูลการตั้งค่าระบบ
    def get_system_settings(self) -> SystemSettings:
        data = self.config.get('system', {})
        return SystemSettings(
            ocrEngine=data.get('ocrEngine', "tesseract"),
            delayShutter=data.get('delayShutter', 0),
            delayBeforeReject=data.get('delayBeforeReject', 0),
            rejectionPeriod=data.get('rejectionPeriod', 0),
            numberStickerBeforeDetection=data.get('numberStickerBeforeDetection', 0),
            rotateImage=data.get('rotateImage', 0),
            detectionPercentage=data.get('detectionPercentage', 0),
            detectionResizeImage=data.get('detectionResizeImage', 0),
            saveImage=data.get('saveImage', False),
        )
    
    # อ่านข้อมูลการตั้งค่ากล้อง
    def get_camera_settings(self) -> CameraSettings:
        data = self.config.get('hardware', {}).get('camera', {})
        return CameraSettings(
            ExposureTime=data.get('ExposureTime', 5000),
            AnalogueGain=data.get('AnalogueGain', 0),
            Brightness=data.get('Brightness', 0),
            Contrast=data.get('Contrast', 0),
            Saturation=data.get('Saturation', 0),
            Sharpness=data.get('Sharpness', 0),
            FrameRate=data.get('FrameRate', 0),
        )

    # อ่านข้อมูลการตั้งค่า pins input, output
    def get_gpio_settings(self) -> GPIOSettings:
        data = self.config.get('hardware', {}).get('gpio', {})
        return GPIOSettings(
            LED0=data.get('LED0', 0),
            LED1=data.get('LED1', 0),
            BUZZER=data.get('BUZZER', 0),
            DI0=data.get('DI0', 0),
            DI1=data.get('DI1', 0),
            DO0=data.get('DO0', 0),
            DO1=data.get('DO1', 0),
            L0=data.get('L0', 0),
            L1=data.get('L1', 0),
        )

    # อัพเดทข้อมูลจำนวนชิ้นงาน
    def update_counter(self, ok: int = 0, ng: int = 0) -> None:
        if 'counters' not in self.config:
            self.config['counters'] = {'ok': 0, 'ng': 0}

        self.config['counters']['ok'] += ok
        self.config['counters']['ng'] += ng
        self.save_config()

    # อัพเดทข้อมูล lot, mfg, exp
    def update_template(self, lot: Optional[str] = None, mfg: Optional[str] = None, exp: Optional[str] = None) -> None:
        if 'template' not in self.config:
            self.config['template'] = {}

        if lot is not None:
            self.config['template']['lot'] = lot
        if mfg is not None:
            self.config['template']['mfg'] = mfg
        if exp is not None:
            self.config['template']['exp'] = exp

        self.save_config()

    # อัพเดทข้อมูลกรอบตรวจจับ
    def update_rectangle(self, rect: RectangleSettings):
        if 'hardware' not in self.config:
            self.config['hardware'] = {"rectangle": {}}

        if rect.X1 is not None:
            self.config['hardware']['rectangle']["x1"] = rect.X1
        if rect.Y1 is not None:
            self.config['hardware']['rectangle']["y1"] = rect.Y1
        if rect.X2 is not None:
            self.config['hardware']['rectangle']["x2"] = rect.X2
        if rect.Y2 is not None:
            self.config['hardware']['rectangle']["y2"] = rect.Y2
            
        self.save_config()

    # รีเซ็ตข้อมูลจำนวนชิ้นงาน
    def reset_counters(self) -> None:
        if 'counters' in self.config:
            self.config['counters']['ok'] = 0
            self.config['counters']['ng'] = 0
            self.save_config()

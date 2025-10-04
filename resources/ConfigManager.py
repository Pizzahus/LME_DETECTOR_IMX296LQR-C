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
class CameraSettings:
    zoom: int
    focus: int
    autoFocus: bool
    brightness: int
    contrast: int
    exposure: int
    sensorDelay: int
    saveImage: bool


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
            self._create_default_config()

        with open(self.config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}

    def _create_default_config(self) -> None:
        default_config = {
            'template': {'lot': 'DEFAULT_LOT', 'mfg': 'YYYYMMDD', 'exp': 'YYYYMMDD'},
            'hardware': {
                'camera': {'zoom': 100, 'focus': 170, 'autoFocus': True, 'brightness': 180, 'contrast': 180, 'exposure': 180, 'sensorDelay': 500, 'saveImage': False},
                'gpio': {
                    'LED0': 20, 
                    'LED1': 21, 
                    'BUZZER': 19, 
                    'DI0': 22, 
                    'DI1': 27, 
                    'DO0': 22, 
                    'DO1': 24, 
                    'L0': 12, 
                    'L1': 13
                },
            },
            'counters': {'ok': 0, 'ng': 0},
        }
        self.save_config(default_config)

    def save_config(self, config: Dict[str, Any] = None) -> None:
        with open(self.config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config or self.config, f, sort_keys=False, allow_unicode=True)

    def get_template(self) -> TemplateLME:
        data = self.config.get('template', {})
        return TemplateLME(
            lot=data.get('lot', ''),
            mfg=data.get('mfg', ''),
            exp=data.get('exp', ''),
        )

    def get_rectangle(self) -> RectangleSettings:
        data = self.config.get('hardware', {}).get('rectangle', {})
        return RectangleSettings(
            X1=data.get('x1', ''),
            X2=data.get('x2', ''),
            Y1=data.get('y1', ''),
            Y2=data.get('y2', ''),
        )

    def get_count(self) -> Counter:
        data = self.config.get('counters', {})
        return Counter(
            ok=data.get('ok', 0),
            ng=data.get('ng', 0),
        )

    def get_camera_settings(self) -> CameraSettings:
        data = self.config.get('hardware', {}).get('camera', {})
        return CameraSettings(
            zoom=data.get('zoom', 0),
            focus=data.get('focus', 0),
            autoFocus=data.get('autoFocus', True),
            brightness=data.get('brightness', 0),
            contrast=data.get('contrast', 0),
            exposure=data.get('exposure', 0),
            sensorDelay=data.get('sensorDelay', 0),
            saveImage=data.get('saveImage', False),
        )

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

    def update_counter(self, ok: int = 0, ng: int = 0) -> None:
        if 'counters' not in self.config:
            self.config['counters'] = {'ok': 0, 'ng': 0}

        self.config['counters']['ok'] += ok
        self.config['counters']['ng'] += ng
        self.save_config()

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

    def reset_counters(self) -> None:
        if 'counters' in self.config:
            self.config['counters']['ok'] = 0
            self.config['counters']['ng'] = 0
            self.save_config()

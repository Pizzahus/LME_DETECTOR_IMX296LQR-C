import yaml
from pathlib import Path
from typing import Dict, Any


class ConfigManager:
    def __init__(self, config_path: str = 'config.yaml'):
        self.config_path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """โหลดการตั้งค่าจากไฟล์ YAML"""
        if not self.config_path.exists():
            self._create_default_config()

        with open(self.config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}

    def _create_default_config(self) -> None:
        """สร้างไฟล์การตั้งค่าเริ่มต้น"""
        default_config = {
            'template': {'lme': {'lot': 'DEFAULT_LOT', 'mfg': 'YYYYMMDD', 'exp': 'YYYYMMDD'}},
            'hardware': {
                'camera': {'zoom': 100, 'focus': 170, 'autoFocus': True, 'brightness': 180, 'contrast': 180, 'exposure': 180, 'sensorDelay': 500, 'saveImage': False},
                'gpio': {'sensorPin': 23, 'buzzerPin': 12},
            },
            'counters': {'ok': 0, 'ng': 0},
        }
        self.save_config(default_config)

    def save_config(self, config: Dict[str, Any] = None) -> None:
        """บันทึกการตั้งค่าลงไฟล์"""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config or self.config, f, sort_keys=False, allow_unicode=True)

    def get_camera_settings(self) -> Dict[str, Any]:
        """ดึงการตั้งค่ากล้อง"""
        return self.config.get('hardware', {}).get('camera', {})

    def get_gpio_settings(self) -> Dict[str, int]:
        """ดึงการตั้งค่า GPIO"""
        return self.config.get('hardware', {}).get('gpio', {})

    def update_counter(self, ok: int = 0, ng: int = 0) -> None:
        """อัพเดทค่าสถิติ"""
        if 'counters' not in self.config:
            self.config['counters'] = {'ok': 0, 'ng': 0}

        self.config['counters']['ok'] += ok
        self.config['counters']['ng'] += ng
        self.save_config()

    def reset_counters(self) -> None:
        """รีเซ็ตค่าสถิติ"""
        if 'counters' in self.config:
            self.config['counters']['ok'] = 0
            self.config['counters']['ng'] = 0
            self.save_config()

    def update_template(self, lot: str = None, mfg: str = None, exp: str = None) -> None:
        """อัพเดทเทมเพลต LME"""
        if 'template' not in self.config:
            self.config['template'] = {'lme': {}}

        if lot is not None:
            self.config['template']['lme']['lot'] = lot
        if mfg is not None:
            self.config['template']['lme']['mfg'] = mfg
        if exp is not None:
            self.config['template']['lme']['exp'] = exp

        self.save_config()

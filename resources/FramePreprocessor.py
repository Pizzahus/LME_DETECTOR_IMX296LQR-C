import cv2
import numpy as np

class FramePreprocessor:
    def __init__(self,
                 threshold_block_size: int = 31,
                 threshold_C: int = 15,
                 morph_kernel_size: tuple = (2, 2),
                 clahe_clip_limit: float = 2.0,
                 clahe_tile_grid_size: tuple = (8, 8),
                 sharpen: bool = True,
                 use_adaptive_threshold: bool = True,
                 use_morphological_open: bool = True,
                 use_otsu_threshold: bool = True,
                 use_clahe: bool = True,
                 use_sharpen: bool = True,
                ):
        
        self.threshold_block_size = threshold_block_size
        self.threshold_C = threshold_C
        self.morph_kernel_size = morph_kernel_size
        self.clahe_clip_limit = clahe_clip_limit
        self.clahe_tile_grid_size = clahe_tile_grid_size
        self.sharpen = sharpen

        self.use_adaptive_threshold= use_adaptive_threshold
        self.use_morphological_open= use_morphological_open
        self.use_otsu_threshold = use_otsu_threshold
        self.use_clahe = use_clahe
        self.use_sharpen = use_sharpen

    def update_parameters(self, 
                         threshold_block_size: int = None,
                         threshold_C: int = None,
                         morph_kernel_size: tuple = None,
                         clahe_clip_limit: float = None,
                         clahe_tile_grid_size: tuple = None,
                         sharpen: bool = None,
                         use_adaptive_threshold: bool = None,
                         use_morphological_open: bool = None,
                         use_otsu_threshold: bool = None,
                         use_clahe: bool = None,
                         use_sharpen: bool = None) -> None:
        """
        อัพเดทพารามิเตอร์การ preprocessing
        
        Args:
            threshold_block_size: ขนาดบล็อกสำหรับ adaptive threshold
            threshold_C: ค่าคงที่สำหรับ adaptive threshold
            morph_kernel_size: ขนาด kernel สำหรับ morphological operation
            clahe_clip_limit: ค่า clip limit สำหรับ CLAHE
            clahe_tile_grid_size: ขนาด grid สำหรับ CLAHE
            sharpen: ใช้ sharpening หรือไม่
            use_adaptive_threshold: ใช้ adaptive threshold หรือไม่
            use_morphological_open: ใช้ morphological opening หรือไม่
            use_otsu_threshold: ใช้ Otsu threshold หรือไม่
            use_clahe: ใช้ CLAHE หรือไม่
            use_sharpen: ใช้ sharpening หรือไม่
        """
        
        if threshold_block_size is not None:
            # ตรวจสอบว่าเป็นเลขคี่
            if threshold_block_size % 2 == 0:
                threshold_block_size += 1
                print(f"Warning: threshold_block_size ถูกปรับเป็นเลขคี่: {threshold_block_size}")
            self.threshold_block_size = threshold_block_size
        
        if threshold_C is not None:
            self.threshold_C = threshold_C
        
        if morph_kernel_size is not None:
            self.morph_kernel_size = morph_kernel_size
        
        if clahe_clip_limit is not None:
            self.clahe_clip_limit = clahe_clip_limit
        
        if clahe_tile_grid_size is not None:
            self.clahe_tile_grid_size = clahe_tile_grid_size
        
        if sharpen is not None:
            self.sharpen = sharpen
        
        if use_adaptive_threshold is not None:
            self.use_adaptive_threshold = use_adaptive_threshold
        
        if use_morphological_open is not None:
            self.use_morphological_open = use_morphological_open
        
        if use_otsu_threshold is not None:
            self.use_otsu_threshold = use_otsu_threshold
        
        if use_clahe is not None:
            self.use_clahe = use_clahe
        
        if use_sharpen is not None:
            self.use_sharpen = use_sharpen

    def update_preprocessing_steps(self, steps_config: dict) -> None:
        """
        อัพเดทขั้นตอน preprocessing จาก dictionary
        
        Args:
            steps_config: dictionary ที่มี key เป็นชื่อ step และ value เป็น boolean
        """
        step_mapping = {
            'adaptive_threshold': 'use_adaptive_threshold',
            'morphological_opening': 'use_morphological_open',
            'otsu_threshold': 'use_otsu_threshold',
            'clahe_contrast': 'use_clahe',
            'sharpening': 'use_sharpen'
        }
        
        for step_name, enabled in steps_config.items():
            if step_name in step_mapping:
                attr_name = step_mapping[step_name]
                setattr(self, attr_name, enabled)
            else:
                print(f"Warning: Unknown preprocessing step '{step_name}'")

    def get_current_settings(self) -> dict:
        """
        ดึงค่าพารามิเตอร์ปัจจุบันทั้งหมด
        
        Returns:
            dictionary ที่มีค่าพารามิเตอร์ทั้งหมด
        """
        return {
            'threshold_block_size': self.threshold_block_size,
            'threshold_C': self.threshold_C,
            'morph_kernel_size': self.morph_kernel_size,
            'clahe_clip_limit': self.clahe_clip_limit,
            'clahe_tile_grid_size': self.clahe_tile_grid_size,
            'sharpen': self.sharpen,
            'use_adaptive_threshold': self.use_adaptive_threshold,
            'use_morphological_open': self.use_morphological_open,
            'use_otsu_threshold': self.use_otsu_threshold,
            'use_clahe': self.use_clahe,
            'use_sharpen': self.use_sharpen
        }

    def reset_to_default(self) -> None:
        """
        รีเซ็ตค่าพารามิเตอร์ทั้งหมดเป็นค่าเริ่มต้น
        """
        self.threshold_block_size = 31
        self.threshold_C = 15
        self.morph_kernel_size = (2, 2)
        self.clahe_clip_limit = 2.0
        self.clahe_tile_grid_size = (8, 8)
        self.sharpen = True
        self.use_adaptive_threshold = True
        self.use_morphological_open = True
        self.use_otsu_threshold = True
        self.use_clahe = True
        self.use_sharpen = True

    def process(self, frame: np.ndarray) -> np.ndarray:
        # Convert to grayscale
        if len(frame.shape) == 3:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Adaptive threshold - ตรวจสอบให้แน่ใจว่าค่าเป็น integer
        if self.use_adaptive_threshold:
            # ตรวจสอบว่า threshold_block_size เป็นเลขคี่ (ตาม requirement ของ OpenCV)
            block_size = self.threshold_block_size
            if block_size % 2 == 0:
                block_size += 1
                
            frame = cv2.adaptiveThreshold(
                frame, 
                255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,
                block_size,
                self.threshold_C
            )

        # Morphological opening
        if self.use_morphological_open:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, self.morph_kernel_size)
            frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)

        # Otsu threshold
        if self.use_otsu_threshold:
            _, frame = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Adaptive contrast enhancement
        if self.use_clahe:
            clahe = cv2.createCLAHE(
                clipLimit=self.clahe_clip_limit, 
                tileGridSize=self.clahe_tile_grid_size
            )
            frame = clahe.apply(frame)

        # Optional sharpening
        if self.use_sharpen:
            kernel_sharp = np.array([[0, -1, 0],
                                     [-1, 5, -1],
                                     [0, -1, 0]])
            frame = cv2.filter2D(frame, -1, kernel_sharp)

        return frame
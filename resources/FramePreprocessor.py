import cv2
import numpy as np

class FramePreprocessor:
    def __init__(self,
                 threshold_block_size: int = 31,
                 threshold_C: int = 15,
                 morph_kernel_size: tuple = (2, 2),
                 clahe_clip_limit: float = 2.0,
                 clahe_tile_grid_size: tuple = (8, 8),
                 sharpen: bool = True):
        self.threshold_block_size = threshold_block_size
        self.threshold_C = threshold_C
        self.morph_kernel_size = morph_kernel_size
        self.clahe_clip_limit = clahe_clip_limit
        self.clahe_tile_grid_size = clahe_tile_grid_size
        self.sharpen = sharpen

    def process(self, frame: np.ndarray) -> np.ndarray:
        # Convert to grayscale
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Adaptive threshold
        frame = cv2.adaptiveThreshold(frame, 255,
                                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY,
                                      self.threshold_block_size,
                                      self.threshold_C)

        # Morphological opening
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, self.morph_kernel_size)
        frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)

        # Otsu threshold
        frame = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # Adaptive contrast enhancement
        clahe = cv2.createCLAHE(clipLimit=self.clahe_clip_limit, tileGridSize=self.clahe_tile_grid_size)
        frame = clahe.apply(frame)

        # Optional sharpening
        if self.sharpen:
            kernel_sharp = np.array([[0, -1, 0],
                                     [-1, 5, -1],
                                     [0, -1, 0]])
            frame = cv2.filter2D(frame, -1, kernel_sharp)

        return frame
import os
from typing import Optional

import cv2
import imutils


def load_image(path: str, height: Optional[int] = None, width: Optional[int] = None):
    assert os.path.exists(path)
    img = cv2.imread(path)
    if height or width:
        img = imutils.resize(img, height=height, width=width)
    return img

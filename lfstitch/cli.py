import os
import glob
import argparse

import cv2

from .stitch import Stitcher
from .utils import load_image


def _parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, default="images")
    parser.add_argument("--output", type=str, default="stitched.jpg")
    args = parser.parse_args()
    return args


def stitch():
    args = _parse()
    img_paths = sorted(glob.glob(f"{args.dir}/*"))
    images = [load_image(path, height=9500) for path in img_paths]
    stitched = Stitcher().blend(images[0], images[1])
    cv2.imwrite(args.output, stitched)

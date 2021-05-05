import os
import glob
import argparse

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
    img_paths = sorted(glob.glob(arg.dir))
    images = [load_image(path) for path in img_paths]
    stitched = Stitcher().blend(images[0], images[1])
    cv2.imwrite(args.output, stitched)

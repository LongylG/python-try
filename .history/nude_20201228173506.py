import sys
import os
import _io
from collections import namedtuple
from PIL import Image


class Nude:
    Skin = namedtuple("Skin", "id skin region x y")

    def __init__(self, path_or_image):
        if isinstance(path_or_image, Image.Image):
            self.image = path_or_image
        elif isinstance(path_or_image, str):
            self.image = Image.open(path_or_image)

        # 获取图片所有的颜色通道
        banks = self.image.getbands()

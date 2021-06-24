import sys
import os
import _io
from collections import namedtuple
from PIL import Image


class Nude:
    Skin = namedtuple("Skin", "id skin region x y")


def __init__(self, path_or_image):
    if isinstance(path_or_image, Image.Image)

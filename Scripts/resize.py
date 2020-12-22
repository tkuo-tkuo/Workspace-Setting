#!/usr/bin/python
from PIL import Image
import os, sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--folder_path', type=str, required=True)
opts = parser.parse_args()

# python resize.py --folder_path "C:/Users/nmake/Desktop/CS/U-2-Net/images"
path = opts.folder_path
dirs = os.listdir(path)
RESIZE_SHAPE = (128, 128)

for item in dirs:
    if os.path.isfile(f'{path}/{item}'):
        im = Image.open(f'{path}/{item}')
        imResize = im.resize(RESIZE_SHAPE, Image.ANTIALIAS)
        imResize.save(f'{path}/{item}')
        print(f'Resize {path}/{item} to {RESIZE_SHAPE}')

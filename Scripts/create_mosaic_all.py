#!/usr/bin/python
from PIL import Image
import os

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

path1 = "C:/Users/nmake/Desktop/CS/U-2-Net/images"
path2 = "C:/Users/nmake/Desktop/CS/U-2-Net/merge"
interval = 5000 
start = 1000000
end =   1095000
NUM_ROWS = 30
RESIZE_SHAPE = (128, 128)
STORE_NAME = 'mosaic_all.png'

dirs = os.listdir(path1)
rows = [None for _ in range(NUM_ROWS)]
for item_ind, item in enumerate(dirs):
    row_ind = item_ind
    if item_ind >= NUM_ROWS:
        break 

    im = Image.open(f'{path1}/{item}')
    rows[row_ind] = im.resize(RESIZE_SHAPE, Image.ANTIALIAS)
    
    item = item.replace('.jpg', '.png')
    for model_iteration in range(start, end+1, interval):
        model_iteration = str(model_iteration).zfill(7)
        rows[row_ind] = get_concat_h(rows[row_ind], Image.open(f'{path2}/{model_iteration}_{item}'))

img = None 
for row in rows:
    if img is None:
        img = row 
    else:
        img = get_concat_v(img, row)

img.save(STORE_NAME)
print('Done!')

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
NUM_ROWS = 10
NUM_COLS = 5
RESIZE_SHAPE = (128, 128)
BASE_STORE_NAME = 'mosaic.png'

for model_iteration in range(start, end+1, interval):
    model_iteration = str(model_iteration).zfill(7)

    dirs = os.listdir(path1)
    rows = [None for _ in range(NUM_ROWS)]
    for item_ind, item in enumerate(dirs):
        if item_ind >= NUM_COLS * NUM_ROWS:
            break 

        row_ind = int(item_ind/NUM_COLS)
        col_ind = item_ind % NUM_COLS 

        im = Image.open(f'{path1}/{item}')
        im = im.resize(RESIZE_SHAPE, Image.ANTIALIAS)
        
        if rows[row_ind] is None:
            rows[row_ind] = im
        else:
            rows[row_ind] = get_concat_h(rows[row_ind], im)

        item = item.replace('.jpg', '.png')
        rows[row_ind] = get_concat_h(rows[row_ind], Image.open(f'{path2}/{model_iteration}_{item}'))

    img = None 
    for row in rows:
        if img is None:
            img = row 
        else:
            img = get_concat_v(img, row)

    img.save(f'{model_iteration}_{BASE_STORE_NAME}')
    print(f'Store {model_iteration}_{BASE_STORE_NAME}')

import imageio
images = []
for model_iteration in range(start, end+1, interval):
    model_iteration = str(model_iteration).zfill(7)
    images.append(imageio.imread(f'{model_iteration}_{BASE_STORE_NAME}'))
    os.remove(f'{model_iteration}_{BASE_STORE_NAME}')

imageio.mimsave('mosaic.gif', images)
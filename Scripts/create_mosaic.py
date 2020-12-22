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

#################################################################################
# Parameters 
#################################################################################
prefix = "C:/Users/nmake/Desktop/CS/U-2-Net"
paths = ["images", "merge", "tune"]
NUM_ROWS, NUM_COLS = 25, 10
RESIZE_SHAPE = (128, 128)
STORE_NAME = 'mosaic.png'
#################################################################################

assert len(paths) >= 1 
dirs = os.listdir(f'{prefix}/{paths[0]}')
rows = [None for _ in range(NUM_ROWS)]

for item_ind, item in enumerate(dirs):
    if item_ind >= NUM_COLS * NUM_ROWS:
        break # We get the number of pieces we need! 

    row_ind = int(item_ind/NUM_COLS)

    for path in paths:
        try:
            im = Image.open(f'{prefix}/{path}/{item}')
        except:
            item_ = item.replace('.jpg', '.png')
            im = Image.open(f'{prefix}/{path}/{item_}')

        im = im.resize(RESIZE_SHAPE, Image.ANTIALIAS)
        print(im)
        rows[row_ind] = im if rows[row_ind] is None else get_concat_h(rows[row_ind], im)

img = None 
for row in rows:
    img = row if img is None else get_concat_v(img, row)

# img.save(STORE_NAME)
print('Done!')

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
path3 = "C:/Users/nmake/Desktop/CS/U-2-Net/tune"
store_folder = "C:/Users/nmake/Desktop/Scripts/temp"

RESIZE_SHAPE = (128, 128)
INCLUDE_RESULT_TWOPATINERS = True 
INCLUDE_RESULT_TWOPATINERS_COLOR_TUNE = True 

dirs = os.listdir(path1)
for item in (dirs):
    print(f'Creating pairs for {item}')
    im = Image.open(f'{path1}/{item}')
    im = im.resize(RESIZE_SHAPE, Image.ANTIALIAS)
    
    if INCLUDE_RESULT_TWOPATINERS:
        # Assume default extension is .jpg
        try: 
            im = get_concat_h(im, Image.open(f'{path2}/{item}'))
        except:
            item_ = item.replace('.jpg', '.png')
            im = get_concat_h(im, Image.open(f'{path2}/{item_}'))

    if INCLUDE_RESULT_TWOPATINERS_COLOR_TUNE:
        item_ = item.replace('.jpg', '.png')
        im = get_concat_h(im, Image.open(f'{path3}/{item_}'))

    im.save(f'{store_folder}/{item}')

print('Done!')

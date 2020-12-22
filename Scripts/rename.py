# Use temp_fns to avoid we have same file name in old files and renamed files 

import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder_path', type=str, required=True)
    opts = parser.parse_args()
    opts.folder_path = "C:/Users/nmake/Desktop/Datasets/Selfie2Anime (UGATIT)/Human/merge"
    # opts.folder_path = "C:/Users/nmake/Desktop/CS/U-2-Net/images"

    fns = [fn for fn in os.listdir(opts.folder_path) if fn.endswith(('.jpg', '.png'))]
    # fns = sorted(fns, key=len)

    temp_fns, rename_fns = [], []
    for idx, fn in enumerate(fns):
        if fn.endswith(('.jpg')):
            new_fn = str(idx).zfill(5)+'.jpg'
        else:
            new_fn = str(idx).zfill(5)+'.png'
        
        os.rename(os.path.join(opts.folder_path, fn), os.path.join(opts.folder_path, '_____'+new_fn))
        temp_fns.append('_____'+new_fn)
        rename_fns.append(new_fn)

    for temp_fn, rename_fn in zip(temp_fns, rename_fns):
        os.rename(os.path.join(opts.folder_path, temp_fn), os.path.join(opts.folder_path, rename_fn))
        print(rename_fn)
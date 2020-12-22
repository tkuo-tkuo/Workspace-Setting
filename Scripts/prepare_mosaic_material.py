import os 
from shutil import copyfile

all = False 

def mv_folder_content(source_folder, dest_folder):
    for fn in os.listdir(source_folder):
        os.rename(f'{source_folder}/{fn}', f'{dest_folder}/{fn}')

def cp_folder_content(source_folder, dest_folder):
    for fn in os.listdir(source_folder):
        copyfile(f'{source_folder}/{fn}', f'{dest_folder}/{fn}')

# 1. Empty all folders which will be used later 
os.system(f'python clear_folders.py')

# 2. Activate u2net_test.py & u2net_remove.py
os.system(f'cd ../CS/U-2-Net/ && python u2net_test.py && python u2net_remove.py')

# 3. U-GAT-IT (painter2)
# U-2-Net/remove → UGATIT/temp_input → UGATIT/temp_output → U-2-Net/anime_face_images 
mv_folder_content('C:/Users/nmake/Desktop/CS/U-2-Net/remove', 'C:/Users/nmake/Desktop/CS/UGATIT-pytorch/temp_input')
if all: 
    os.system(f'cd ../CS/UGATIT-pytorch/ && python main.py --phase produce_all')
else:
    os.system(f'cd ../CS/UGATIT-pytorch/ && python main.py --phase produce')
mv_folder_content('C:/Users/nmake/Desktop/CS/UGATIT-pytorch/temp_output', 'C:/Users/nmake/Desktop/CS/U-2-Net/anime_face_images')

# 4. CartoonGAN (painter1)
# U-2-Net/images → CartoonGAN/test_img → CartoonGAN/test_outputs → U-2-Net/anime_background_images 
cp_folder_content('C:/Users/nmake/Desktop/CS/U-2-Net/images', 'C:/Users/nmake/Desktop/CS/CartoonGAN-Test-Pytorch-Torch/test_img')
os.system(f'cd ../CS/CartoonGAN-Test-Pytorch-Torch && python test.py')
mv_folder_content('C:/Users/nmake/Desktop/CS/CartoonGAN-Test-Pytorch-Torch/test_output', 'C:/Users/nmake/Desktop/CS/U-2-Net/anime_background_images')

# 5. Resize 
os.system('python resize.py --folder_path "C:/Users/nmake/Desktop/CS/U-2-Net/results"')
os.system('python resize.py --folder_path "C:/Users/nmake/Desktop/CS/U-2-Net/anime_background_images"')

# 6. Merge 
if all:
    os.system(f'cd ../CS/U-2-Net/ && python u2net_merge_all.py')
else:
    os.system(f'cd ../CS/U-2-Net/ && python u2net_merge.py')

# 7. Tune back the color tone 
if all:
    # PENDING
    # os.system(f'cd ../CS/U-2-Net/ && python u2net_tune_color_all.py')
    pass 
else:
    os.system(f'cd ../CS/U-2-Net/ && python u2net_tune_color.py')

# 8. Turn folder to npy for further evaluation (FID/KID), this procedure should be optional 
os.system(f'cd ../CS/U-2-Net/ &&\
    python folder2npy.py --folder_path images &&\
    python folder2npy.py --folder_path merge &&\
    python folder2npy.py --folder_path tune')
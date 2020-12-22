import os 

def empty_folder(path):
    print(f'Start clearning {path}')
    for fn in os.listdir(path):
        if fn.endswith('.jpg') or fn.endswith('.png'):
            os.remove(f'{path}/{fn}')

for folder_name in (['results', 'remove', 'merge', 'background', 'anime_face_images', 'anime_background_images', 'tune']):
    empty_folder(f'C:/Users/nmake/Desktop/CS/U-2-Net/{folder_name}')
for folder_name in (['test_img', 'test_output']):
    empty_folder(f'C:/Users/nmake/Desktop/CS/CartoonGAN-Test-Pytorch-Torch/{folder_name}')
for folder_name in (['temp_input', 'temp_output']):
    empty_folder(f'C:/Users/nmake/Desktop/CS/UGATIT-pytorch/{folder_name}')
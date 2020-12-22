''' Remainder
- Remember to revise your image pattern 
'''

import os 
FPS = 30 # frame per second 

# Create video 1 (left video)
os.system(f'ffmpeg -r {FPS} -i ../CS/U-2-Net/images/%05d.jpg -c:v libx264 -r 30 -pix_fmt yuv420p left.mp4')

# create video 2 (right video)
os.system(f'ffmpeg -r {FPS} -i ../CS/U-2-Net/merge/%05d.png -c:v libx264 -r 30 -pix_fmt yuv420p right.mp4')

# Merge video 1 and video via ffmpeg 
os.system(f'ffmpeg -i left.mp4 -i right.mp4 -filter_complex hstack merge.mp4')
os.remove('left.mp4')
os.remove('right.mp41')

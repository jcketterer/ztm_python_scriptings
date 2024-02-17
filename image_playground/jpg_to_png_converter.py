import sys
import os
from PIL import Image


# grab first and second argument
img_folder = sys.argv[1]
output_folder = sys.argv[2]


# check if new exists and if not create the folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through pokedex, and convert images to PNG

for filename in os.listdir(img_folder):
    img = Image.open(f'{img_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]

    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')

# finally save to new folder
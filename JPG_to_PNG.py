# Use your Terminal, if you are on 
# windows type: python JPG_to_PNG.py JPG/ PNG/
# It will create a new folder 
# and put your PNGs in this folder.
import sys
import os
from PIL import Image

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)


for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{path}{filename}')
    img.save(f'{directory}/{clean_name}.png', 'png')
    print('all done!')

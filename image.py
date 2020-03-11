import sys
import os
import argparse
import PIL
from PIL import Image

#grab first and second argument
parser = argparse.ArgumentParser(description='jpg to png')
parser.add_argument('--input', '-i', type=str, help='İnput directory for images')
parser.add_argument('--output','-o',type=str, help='output directory for new images')
args = parser.parse_args()
#check if new folder exist it not create
print(args.output)
cwd = os.getcwd()
image_path = os.path.join(cwd, args.input)

new_path = os.path.join(cwd, args.output)
isdir = os.path.isdir(new_path)
if not isdir:
    os.makedirs(args.output)

#convert images to png
images = []
png_suffix = 'png'
for path, directory, files in os.walk(image_path):
    for img_file in files:
        filename, file_ext = os.path.splitext(img_file)

        jpg_file = os.path.join(image_path, img_file)
        png_image = os.path.join(new_path, filename +'.'+png_suffix)
        print(png_image)


        Image.open(jpg_file, 'r').save(png_image)
        #print(filename)
        



    
    
  
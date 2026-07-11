import sys
import os
from PIL import Image

# command: python jpg_to_png_converter.py Pokedex/ new/

# getting the file path
processing_folder = sys.argv[1]
result_folder = sys.argv[2]

# check the folder exists
if not os.path.exists(result_folder):
    os.makedirs(result_folder)


def convert_to_png(image_file):
    img = Image.open(f"{processing_folder}{image_file}")
    # new_file_name = f"{image_file.split(".")[0]}.png"
    clean_name = f"{os.path.splitext(image_file)[0]}.png"
    img.save(f"./{result_folder}{clean_name}", "png")


# getting all the files of Pokedex folder
for file in os.listdir(processing_folder):
    convert_to_png(file)

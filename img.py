import sys
import os
from PIL import Image


# Grab the source folder and the target folder
img_folder, target_folder = sys.argv[1], sys.argv[2]

# Check if the target folder exists, if not, create it
if not os.path.exists(target_folder):
    os.makedirs(target_folder)


print(os.listdir(img_folder))

# Open the source folder and iterate over each file to convert them
# for filename in os.listdir(img_folder):
#     # Grab the image
#     img = Image.open(f'{img_folder}{filename}')
#     formatted_path_name = os.path.splitext(filename)[0]
#     img.save(f'{target_folder}{formatted_path_name}.png','png')
#     print(f'{filename} Modified and stored in {target_folder}')
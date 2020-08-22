#!/usr/bin/env python3

import os
from PIL import Image
from pprint import pprint


path_to_save_images = os.path.expanduser("~/supplier-data/images")
logs = []

def check_directory_exist(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def convert_images(size,extension):
    for filename in os.listdir(path_to_save_images):
        if filename.endswith('.TIFF'):
            location = "{}/{}".format(path_to_save_images, filename)
            try:
                with Image.open(location) as img:
                    img.convert("RGB").resize(size).save("{}.{}".format(location.split(".")[0],extension), quality=100)
                os.remove(location) #check 
            except Exception as e:
                logs.append(str(e))


def main():
    to_size = 600, 400 #check
    check_directory_exist(path_to_save_images)
    convert_images(size=to_size,extension="jpeg")
    if(logs):
        print("Errors:")
        pprint(logs)

if __name__ == "__main__":
    main()

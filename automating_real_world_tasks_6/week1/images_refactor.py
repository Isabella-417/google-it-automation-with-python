#!/usr/bin/python3

import os
from PIL import Image


directory_path = "images"
new_directory = "opt/icons/" #"/opt/icons/"

# parameters
size = 128, 128
rotation = 90
extension = "JPEG"

logs = []

def main():
    for filename in os.listdir(directory_path):
        if not filename.startswith('.'):
            location = "{}/{}".format(directory_path, filename)
            try:
                with Image.open(location) as img:
                    img.convert("RGB").rotate(90).resize((size)).save(
                        "{}{}_edited".format(new_directory, filename), extension, quality=100)
            except Exception as e:
                logs.append(str(e))


if __name__ == "__main__":
    main()

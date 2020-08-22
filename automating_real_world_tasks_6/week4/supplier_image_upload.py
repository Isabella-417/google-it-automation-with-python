#!/usr/bin/env python3
import requests
import os

path_to_save_images = os.path.expanduser("~/supplier-data/images")


def upload_images_to_server(url):
    for filename in os.listdir(path_to_save_images):
        if filename.endswith(".jpeg"):
            path = "{}/{}".format(path_to_save_images,filename)
            with open(path, 'rb') as opened:
                try:
                    response = requests.post(url, files={'file': opened})
                except requests.exceptions.RequestException as e:
                    raise SystemExit(e)
                if response.status_code != 201:
                    print("Error occurs")
                    break

def main():
    url = "http://34.72.240.124/upload/"
    upload_images_to_server(url)


if __name__ == "__main__":
    main()
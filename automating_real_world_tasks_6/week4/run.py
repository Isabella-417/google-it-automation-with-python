#!/usr/bin/env python3
import os
import requests
import json

#extract information in all the files given a directory path
def extract_data_from_files(directory_path):
    fruits_notes = []
    for filename in os.listdir(directory_path):
        path = "{}{}".format(directory_path, filename)
        with open(path) as file:
            lines = file.readlines()
            fruits_dict = {}
            fruits_dict["name"] = lines[0].strip()
            fruits_dict["weight"] = int(lines[1].strip().split(" lbs")[0])
            fruits_dict["description"] = lines[2].strip()
            fruits_dict["image_name"] = "{}.jpeg".format(filename.split(".")[0])
            fruits_notes.append(fruits_dict)
    return fruits_notes

# Make a post to create new register given an array of obj
def submit_fruits(arr_json_fruits):
    endpoint = "http://[linux-instance-external-IP]/fruits/"

    for fruit in arr_json_fruits:
        #print("info: {}={}={}".format(endpoint, fruit,type(fruit)))
        try:
            response = requests.post(endpoint, json=fruit)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        #print("response: {}={}".format(response.content,type(response)))
        #print(response.status_code)
        if response.status_code != 201:
            print("Error occurs")
            break

# Save a given dictionary in json format
def save_dictionary_as_json(fruit_dict):
    with open('fruits.json', 'w') as fruits_json:
        json.dump(fruit_dict, fruits_json, indent=2)

def main():
    file_products_path = os.path.expanduser("~/supplier-data/descriptions/")
    fruits_dict = extract_data_from_files(file_products_path)
    submit_fruits(fruits_dict)
    save_dictionary_as_json(fruits_dict)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from datetime import datetime
import os
import reports
import json

def get_data_from_json_file(json_file_path):
    data = []

    with open(json_file_path, 'r') as fruits_json:
        d = json.load(fruits_json)
        for list_obj_fruit in d:
            data.append(["\nname: {} \nweight: {} lbs".format(list_obj_fruit["name"],list_obj_fruit["weight"])])
        return data

def main():
    path_to_file = os.path.expanduser("~/supplier-data/fruits.json")
    data = get_data_from_json_file(path_to_file)
    date = datetime.today().strftime("%B %d, %Y")

    reports.generate_report("/tmp/processed.pdf", "Processed Update on {}".format(date), data)

if __name__ == "__main__":
    main()

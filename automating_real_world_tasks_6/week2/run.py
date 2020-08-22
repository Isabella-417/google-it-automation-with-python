#!/usr/bin/python3

import os
import requests

directory_path = "/data/feedback/"  # change to /data/feedback


def extract_data_from_files(directory_path):
    feedback_notes = []
    for filename in os.listdir(directory_path):
        path = "{}{}".format(directory_path, filename)
        with open(path) as file:
            lines = file.readlines()
            fb_dict = {}
            fb_dict["title"] = lines[0].strip()
            fb_dict["name"] = lines[1].strip()
            fb_dict["date"] = lines[2].strip()
            fb_dict["feedback"] = lines[3].strip()  # ....
            feedback_notes.append(fb_dict)
    return feedback_notes


def submit_feedback(arr_json_fb):
    endpoint = "http://34.72.137.33/feedback/"
    for feedback in arr_json_fb:
        #print("info: {}={}={}".format(endpoint, feedback,type(feedback)))
        try:
            response = requests.post(endpoint, json=feedback)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)
        #print("response: {}={}".format(response.content,type(response)))
        print(response.status_code)
        if response.status_code != 201:
            print("Error occurs")
            break


def main():
    json_data = extract_data_from_files(directory_path)
    submit_feedback(json_data)

if __name__ == "__main__":
    main()

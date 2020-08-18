#!/usr/bin/env python3
import re
import operator
import csv
import itertools


# Path
log_file_path = "../syslog.log"

# Dicts
user = {}
error = {}

# Regex
error_regex = "(ERROR) ([\w\s\']+) \(\w+\)*"
user_regex = "(INFO|ERROR) ([\w\s\']+)(\[.+?\])*\s(\([a-z\.]+\))*"
#"(INFO|ERROR) ([\w\s\']+)(\[.+?\])*\s(\(\w+\))*"


def add_to_error_dict(element):
    if element.group(2) in error:
        error[element.group(2)] += 1
    else:
        error[element.group(2)] = 1


def add_per_user_dict(element):
    if element.group(4) is not None:
        name = re.sub('[()]', '', element.group(4))
        if name in user:
            user[name][element.group(1)] += 1
        else:
            user[name] = {"ERROR": 0, "INFO": 0}
            user[name][element.group(1)] += 1


def create_error_csv(d, file_name):
    with open(file_name, "w") as csv_file:
        writer = csv.writer(csv_file)
        for key, value in d:
            writer.writerow([key, value])


def create_csv(d, file_name):
    headers = ["USERNAME","INFO","ERROR"]
    with open(file_name, "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)

        for key,value in d:
            writer.writerow([key,value["INFO"],value["ERROR"]])


with open(log_file_path, "r") as file:
    for line in file:
        formated_text = re.search(user_regex, line)
        if formated_text:
            add_per_user_dict(formated_text)

        if "ERROR" in line:
            formated_text = re.search(error_regex, line)
            if formated_text:
                add_to_error_dict(formated_text)

error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
user = sorted(user.items())
error.insert(0, ("Error", "Count"))

create_error_csv(error, "error_message.csv")
create_csv(user, "user_statistics.csv")

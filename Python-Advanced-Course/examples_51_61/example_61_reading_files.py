# Example 61 - Reading files

import json
import csv

file_txt = "output.txt"
file_json = "output.json"
file_csv = "output.csv"

try:
    with open(file=file_txt, mode="r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("You don't have permission to access this file")

try:
    with open(file=file_json, mode="r") as file:
        content = json.load(file)
        print(content["name"])
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("You don't have permission to access this file")

try:
    with open(file=file_csv, mode="r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("You don't have permission to access this file")

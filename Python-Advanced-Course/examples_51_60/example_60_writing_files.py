# Example 60 - Writing files

import json
import csv

file_path_txt = "output.txt"
file_path_json = "output.json"
file_path_csv = "output.csv"

data_txt = "Were you rushing or were you drugging!?"
data_json = {"name": "Terence Fletcher", "age": 52, "Job": "Conductor"}
data_csv = [["name", "age", "job"],
            ["Walter", 50, "Chemist"],
            ["Hank", 45, "DEA Agent"],
            ["Gus", 54, "Restaurant owner"]]

try:
    with open(file=file_path_txt, mode="w", newline="") as file:
        file.write(data_txt + "\n")
        print("Txt file written successfully")
except FileExistsError:
    print("File already exists")

try:
    with open(file=file_path_json, mode="w", newline="") as file:
        json.dump(data_json, file, indent=4)
        print("Json file written successfully")
except FileExistsError:
    print("File already exists")

try:
    with open(file=file_path_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in data_csv:
            writer.writerow(row)
        print("Csv file written successfully")
except FileExistsError:
    print("File already exists")

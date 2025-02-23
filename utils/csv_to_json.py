import csv
import json

def csv_to_json(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        json_data = [row for row in csv_reader]
        return json_data

def save_json_to_file(json_data, json_file_path):
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

def csv_to_json_file(csv_file_path, json_file_path):
    json_data = csv_to_json(csv_file_path)
    save_json_to_file(json_data, json_file_path)
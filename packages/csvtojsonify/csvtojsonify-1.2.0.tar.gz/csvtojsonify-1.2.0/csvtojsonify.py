# csvtojsonify.py

import csv
import json

def convert_csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile)

if __name__ == "__main__":
    # Get the input and output file names from the user
    csv_file = input("Enter the input CSV file name: ")
    json_file = input("Enter the output JSON file name: ")

    # Check if input file name ends with ".csv"
    if not csv_file.endswith(".csv"):
        print("Error: Input file name must end with '.csv'")
        exit(1)

    # Check if output file name ends with ".json"
    if not json_file.endswith(".json"):
        print("Error: Output file name must end with '.json'")
        exit(1)

    # Call the conversion function
    convert_csv_to_json(csv_file, json_file)

    print("Conversion successful! The new JSON file is", json_file)

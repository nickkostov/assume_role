import json
import os
# Open the file for reading
def account_specifics(fpath):
    with open(fpath, 'r') as f:
        # Load the JSON data from the file
        accounts = json.load(f)
    # Extract the Id and Name fields of each account
    for account in accounts:
        id = account['Id']
        name = account['Name']
        print(f"ID: {id}, Name: {name}")
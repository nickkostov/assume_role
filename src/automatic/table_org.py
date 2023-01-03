import boto3
import json
import os
from tqdm import tqdm

# Create an Organizations client
org_client = boto3.client('organizations')

# Call the list_roots method to get the root of the organization
response = org_client.list_roots()

# Get the list of accounts in the root
accounts = org_client.list_accounts_for_parent(ParentId=response['Roots'][0]['Id'])['Accounts']

def table_list_as_json(fpath):
    # Recursively traverse the organizational units and add any accounts found to the list
    def get_accounts_in_unit(unit_id):
        unit_response = org_client.list_accounts_for_parent(ParentId=unit_id)
        accounts.extend(unit_response['Accounts'])
        if 'NextToken' in unit_response:
            get_accounts_in_unit(unit_id, unit_response['NextToken'])

    def get_units_in_unit(unit_id):
        units_response = org_client.list_organizational_units_for_parent(ParentId=unit_id)
        for unit in tqdm(units_response['OrganizationalUnits'], desc="Loading units"):
            get_accounts_in_unit(unit['Id'])
            get_units_in_unit(unit['Id'])

    # Display a progress bar for the entire function
    with tqdm(desc="Loading accounts and units", total=len(accounts)) as pbar:
        get_units_in_unit(response['Roots'][0]['Id'])
        pbar.update()

    # Convert the datetime objects to strings
    for account in accounts:
        account['JoinedTimestamp'] = str(account['JoinedTimestamp'])

    # Convert the accounts list to a JSON object
    json_accounts = json.dumps(accounts)
    print(f"Total number of accounts: {len(accounts)}")

    with open(fpath, 'w') as f:
        # Write the JSON object to the file
        f.write(json_accounts)

#!/usr/bin/env python3
import boto3
from tqdm import tqdm
from prettytable import PrettyTable
# Create an Organizations client
org_client = boto3.client('organizations')

# Call the list_roots method to get the root of the organization
response = org_client.list_roots()

# Get the list of accounts in the root
accounts = org_client.list_accounts_for_parent(ParentId=response['Roots'][0]['Id'])['Accounts']

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
num_units = len(org_client.list_organizational_units_for_parent(ParentId=response['Roots'][0]['Id'])['OrganizationalUnits'])
# Display a progress bar for the entire script
with tqdm(desc="Loading accounts and units", total=num_units) as pbar:
    get_units_in_unit(response['Roots'][0]['Id'])
    pbar.update()


# Create a table
table = PrettyTable()

# Add the table headers
table.field_names = ["Account ID", "Account Name"]

# Add the data to the table
for account in tqdm(accounts, desc="Loading accounts"):
    table.add_row([account['Id'], account['Name']])

# Print the table and the number of accounts
print(table)
print(f"Number of accounts: {len(accounts)}")
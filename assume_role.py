#!/usr/bin/env python3
import boto3
from prettytable import PrettyTable
import subprocess

# Create a session using the specified profile
read_profiles=subprocess.run(["./src/reading/read_profiles.py"])
profile_name = input("Enter the profile that we will be using: ")
session = boto3.Session(profile_name=profile_name)

# Create an STS client using the session
sts_client = session.client('sts')

# Condition if default to not use MFA
if profile_name != "default":
    org_table=subprocess.run(["./src/table_org.py"])
    account_id = input('Enter the Account ID that you want to assume: ')
    read_roles=subprocess.run(["./src/reading/read_roles.py"])
    role_name = input('Enter the name of the role: ')
    read_mfa_account_ids=subprocess.run(["./src/reading/read_mfa_account_ids.py"])
    serial_num_id = input('Enter the MFA Account ID: ')
    read_mfa_names=subprocess.run(["./src/reading/read_mfa_names.py"])
    mfa_name = input('MFA Name: ')
    token_code = input('Enter the MFA token code: ')

    # Assume the role
    response = sts_client.assume_role(
        RoleArn='arn:aws:iam::' + account_id + ':role/' + role_name,
        RoleSessionName='ExampleSession',
        SerialNumber='arn:aws:iam::' + serial_num_id + ':mfa/' + mfa_name,
        DurationSeconds=3600,
        TokenCode=token_code
    )
else:
    print(org_table)
    account_id = input('Enter the Account ID that you want to assume: ')
    role_name = input('Enter the name of the role: ')
    # Assume the role without MFA
    response = sts_client.assume_role(
        RoleArn='arn:aws:iam::' + account_id + ':role/' + role_name,
        RoleSessionName='Assumed Role',
        DurationSeconds=3600
    )

print('-------------------------------------------------------')
print('In order to use them copy-pasta the content: ')
print('export AWS_ACCESS_KEY_ID=' + response['Credentials']['AccessKeyId'])
print('export AWS_SECRET_ACCESS_KEY=' + response['Credentials']['SecretAccessKey'])
print('export AWS_SESSION_TOKEN=' + response['Credentials']['SessionToken'])
print('-------------------------------------------------------')

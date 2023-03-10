#!/usr/bin/env python3
import boto3
import os
from assume.configuration import config

# Global VArs
ASSUME_CONFIG_PATH = os.path.join(os.environ["HOME"], ".assume_config")

# Create a session using the specified profile
config.get_aws_profiles()

profile_name = input("Enter the profile that we will be using: ")
session = boto3.Session(profile_name=profile_name)

# Create an STS client using the session
sts_client = session.client('sts')

# Condition if default to not use MFA
if profile_name != "default":
    from assume.automatic import read_accounts
    read_accounts.account_specifics(os.path.join(ASSUME_CONFIG_PATH, "accounts.json"))
    account_id = input('Enter the Account ID that you want to assume: ')
    # Gets the correct path leading to .assume_config and substitutes the files
    config.readroles(os.path.join(ASSUME_CONFIG_PATH, "roles"))
    role_name = input('Enter the name of the role: ')
    config.mfa_acc_id(os.path.join(ASSUME_CONFIG_PATH, "mfa_account_ids"))
    serial_num_id = input('Enter the MFA Account ID: ')
    config.mfa_read_names(os.path.join(ASSUME_CONFIG_PATH, "mfa_names"))
    mfa_name = input('MFA Name: ')
    token_code = input('Enter the MFA token code: ')

    # Assume the role
    response = sts_client.assume_role(
        RoleArn='arn:aws:iam::' + account_id + ':role/' + role_name,
        RoleSessionName='Operator',
        SerialNumber='arn:aws:iam::' + serial_num_id + ':mfa/' + mfa_name,
        DurationSeconds=3600,
        TokenCode=token_code
    )
else:
    from assume.automatic import table_org, read_accounts
    table_org.table_list_as_json(os.path.join(ASSUME_CONFIG_PATH, "accounts.json"))
    read_accounts.account_specifics(os.path.join(ASSUME_CONFIG_PATH, "accounts.json"))
    account_id = input('Enter the Account ID that you want to assume: ')
    config.readroles(os.path.join(ASSUME_CONFIG_PATH, "roles"))
    role_name = input('Enter the name of the role: ')
    # Assume the role without MFA
    response = sts_client.assume_role(
        RoleArn='arn:aws:iam::' + account_id + ':role/' + role_name,
        RoleSessionName='Operator',
        DurationSeconds=3600
    )

print('-------------------------------------------------------')
print('In order to use them copy-pasta the content: ')
print('export AWS_ACCESS_KEY_ID=' + response['Credentials']['AccessKeyId'])
print('export AWS_SECRET_ACCESS_KEY=' + response['Credentials']['SecretAccessKey'])
print('export AWS_SESSION_TOKEN=' + response['Credentials']['SessionToken'])
print('-------------------------------------------------------')
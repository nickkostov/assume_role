#!/usr/bin/env python3
import boto3

# Create a session using the specified profile
profile_name = input("Enter the profile that we will be using: ")
session = boto3.Session(profile_name=profile_name)

# Create an STS client using the session
sts_client = session.client('sts')

# Prompt the user to enter the name of the role and the MFA token code
account_id = input('Enter the Account ID that you want to assume: ')
role_name = input('Enter the name of the role: ')
#
serial_num_id = input('Enter the MFA Account ID: ')
mfa_name = input('MFA Name: ')
token_code = input('Enter the MFA token code: ')

# Assume the role
response = sts_client.assume_role(
    RoleArn='arn:aws:iam::' + account_id + ':role/' + role_name,
    RoleSessionName='ExampleSession',
    SerialNumber='arn:aws:iam::' + serial_num_id + ':mfa/' + mfa_name,
    TokenCode=token_code
)

# Print the temporary security credentials
print('Access Key ID:', response['Credentials']['AccessKeyId'])
print('Secret Access Key:', response['Credentials']['SecretAccessKey'])
print('Session Token:', response['Credentials']['SessionToken'])

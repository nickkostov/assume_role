#!/usr/bin/env python3
import boto3

# Open the profiles file and read it
with open('profiles', 'r') as f:
    contents = f.read()
string_list = contents.split()

output = '\n'.join(string_list)
print('Your profiles are: \n' + output)

# Create a session using the specified profile
profile_name = input("Enter the profile that we will be using: ")
session = boto3.Session(profile_name=profile_name)

# Create an STS client using the session
sts_client = session.client('sts')
with open('accounts', 'r') as f:
    contents = f.read()
string_list = contents.split()
output = ' '.join(string_list)
print('Your profiles are: ' + output)

# Condition if default to not use MFA
if profile_name != "default":
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
        DurationSeconds=3600
        TokenCode=token_code
    )
else:
    account_id = input('Enter the Account ID that you want to assume: ')
    role_name = input('Enter the name of the role: ')
    # Assume the role without MFA
    response = sts_client.assume_role(
        RoleArn='arn:aws:iam::' + account_id + ':role/' + role_name,
        RoleSessionName='ExampleSession'
        DurationSeconds=3600
    )

# Print the temporary security credentials
print('Your Session Credentials are: ')
print('Access Key ID:', response['Credentials']['AccessKeyId'])
print('Secret Access Key:', response['Credentials']['SecretAccessKey'])
print('Session Token:', response['Credentials']['SessionToken'])

print('In order to use them copy-pasta the content: ')
print('export AWS_ACCESS_KEY_ID=' + response['Credentials']['AccessKeyId'])
print('export AWS_SECRET_ACCESS_KEY=' + response['Credentials']['SecretAccessKey'])
print('export AWS_SESSION_TOKEN=' + response['Credentials']['SessionToken'])
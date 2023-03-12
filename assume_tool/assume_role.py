#!/usr/bin/env python3
import boto3
import os
from assume_tool import configuration

ASSUME_CONFIG_PATH = os.path.join(os.environ["HOME"], ".assume_config")

# Create an STS client using the session
def a_role():
    profile_name = input("Enter the profile that we will be using: ")
    session = boto3.Session(profile_name='ptc-iam')
    sts_client = session.client('sts')
    if profile_name != "default":
        account_id = input('Enter the Account ID that you want to assume: ')
        configuration.readroles(os.path.join(ASSUME_CONFIG_PATH, "roles"))
        role_name = input('Enter the name of the role: ')
        configuration.mfa_acc_id(os.path.join(ASSUME_CONFIG_PATH, "mfa_account_ids"))
        serial_num_id = input('Enter the MFA Account ID: ')
        configuration.mfa_read_names(os.path.join(ASSUME_CONFIG_PATH, "mfa_names"))
        mfa_name = input('MFA Name: ')
        token_code = input('Enter the MFA token code: ')
        # Assume the role
        response = sts_client.assume_role(
            RoleArn='arn:aws:iam::' + account_id + ':role/' + role_name,
            RoleSessionName='Operator',
            SerialNumber='arn:aws:iam::' + serial_num_id + ':mfa/' + mfa_name,
            DurationSeconds=7200,
            TokenCode=token_code
        )

    print('-------------------------------------------------------')
    print('In order to use them copy-pasta the content: ')
    print('export AWS_ACCESS_KEY_ID=' + response['Credentials']['AccessKeyId'])
    print('export AWS_SECRET_ACCESS_KEY=' + response['Credentials']['SecretAccessKey'])
    print('export AWS_SESSION_TOKEN=' + response['Credentials']['SessionToken'])
    print('-------------------------------------------------------')
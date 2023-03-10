#!/usr/bin/env python3
import os

def get_aws_profiles ():
    with open(os.environ['HOME'] + '/.aws/credentials', 'r') as f:
        contents = f.read()
    
    string_list = contents.split('\n')

    for line in string_list:
       if line.startswith("[") and line.endswith("]"):
          res = line[1:-1]
          print(res)

def readroles(fpath):
    with open(fpath, 'r') as f:
        contents = f.read()
    string_list = contents.split()

    output = '\n'.join(string_list)
    print('Available roles are: \n' + output)

def mfa_read_names(fpath):
    with open(fpath, 'r') as f:
        contents = f.read()
    string_list = contents.split()

    output = '\n'.join(string_list)
    print('Your MFA Device Names are: \n' + output)

def mfa_acc_id(fpath):
    with open(fpath, 'r') as f:
        contents = f.read()
    string_list = contents.split()

    output = '\n'.join(string_list)
    print('Your MFA Account IDs are: \n' + output)
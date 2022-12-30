#!/usr/bin/env python3

import os


file_names = ['roles', 'mfa_names', 'mfa_account_ids']
roles = input('Provide a list of your roles separated by coma: ')
mfa_names = input('Provide a list of your MFA devices serparated by coma: ')
mfa_account_ids = input('Provide a list of your MFA devices serparated by coma: ')

contents = [ roles, mfa_names, mfa_account_ids]



def create_config_dir():
  if os.path.exists(os.environ['HOME'] + '/.assume_configuration_folder/'):
    print("Directory already exists.")
  else:
    try:
      os.mkdir(os.environ['HOME'] + '/.assume_configuration_folder/')
    except PermissionError:
      print("Permission denied: Unable to create directory at the specified location.")
create_config_dir()

def create_configuration_files():
    
    for file_name in file_names:
    # Creating the files:
      with open(os.environ['HOME'] + '/.assume_configuration_folder/' + file_name, 'w') as f:
        for i, file_name in enumerate(file_names):
        # Writing what we want:
            with open(os.environ['HOME'] + '/.assume_configuration_folder/' + file_name, 'w') as f:
                f.write(contents[i])
create_configuration_files()
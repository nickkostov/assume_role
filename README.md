# Python Role Assumtion
Python Script that generates the authentication credentials for aws accounts

# How it works:

The script is for the following use case:
- AWS Organization is enabled
  - Listing permissions Required if you are an admin if not you need to create your own accounts.json file.
- You have an API key created in the ORG account
  - Assigned to a user
- You are using a separate IAM account to access other accounts

# Example usage:
Add it to your path:
```bash
export PATH=$PATH:~/.assume_config/assume
```
Create symlink:
Note that this sometimes does not work and you might have to enter the `/usr/local/bin/`

```bash
ln -s path/where/you/cloned/the/reposiory/assume.py /usr/local/bin/assume
```

Note: `assume init` cleans the old configuration and recreates it.

```bash
assume --help
Usage: assume [OPTIONS]
  Run with init if you want to initialize
Options:
  --init          Initialization of configuration directory
  --gen-acc-list  Generates list of AWS Organization Accounts if only you have admin permissions to your ORG account!
  --help          Show this message and exit.
```


This will prompt you for:
```bash
assume
profile-name-from (~/.aws/credentials)
prfoile-name-2
profile-name-3
Enter the profile that we will be using: ptc-iam
ID: 999999999999, Name: Account Name
Enter the Account ID that you want to assume: 
```
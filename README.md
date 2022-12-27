# Python Role Assumtion
Python Script that generates the authentication credentials for aws accounts

# How it works:

The script is for the following use case:
- AWS Organization is enabled
  - Listing permissions Required
- You have an API key created in the ORG account
  - Assigned to a user
- You are using a separate IAM account to access other accounts

# Example usage:

```bash
./assume_role.py
```

This will prompt you for:
```bash
./assume_role.py

Enter the profile that we will be using: default
Enter the Account ID that you want to assume: 2134124124124
Enter the name of the role: role_name
Enter the MFA Account ID: 2134141241245
MFA Name: NAME_OF_MFA_DEVICE
```

You will have to create the following files in order to fit the best user case:

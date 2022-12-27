#!/usr/bin/env python3

# Open the profiles file and read it
with open('mfa_names', 'r') as f:
    contents = f.read()
string_list = contents.split()

output = '\n'.join(string_list)
print('Your MFA Device Names are: \n' + output)
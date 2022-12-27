#!/usr/bin/env python3

# Open the profiles file and read it
with open('roles', 'r') as f:
    contents = f.read()
string_list = contents.split()

output = '\n'.join(string_list)
print('Available roles are: \n' + output)
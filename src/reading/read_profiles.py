#!/usr/bin/env python3

# Open the profiles file and read it
with open('profiles', 'r') as f:
    contents = f.read()
string_list = contents.split()

output = '\n'.join(string_list)
print('Your Profiles are: \n' + output)
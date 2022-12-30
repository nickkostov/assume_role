#!/usr/bin/env python3
import os 
# Open the profiles file and read it

def get_aws_profiles ():
    with open(os.environ['HOME'] + '/.aws/credentials', 'r') as f:
        contents = f.read()
    
    string_list = contents.split('\n')
    
    
    for line in string_list:
       if line.startswith("[") and line.endswith("]"):
          res = line[1:-1]
          print(res)
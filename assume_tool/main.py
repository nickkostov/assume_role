import argparse

from assume_tool.configuration import print_profiles
#from assume_tool.configuration import generate_credentials
from assume_tool.assume_role import a_role

def main():
    argument = argparse.ArgumentParser(
     description = "A simple CLI that will allow you perform quick but crucial tasks!",
     formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    argument.add_argument('--print-profiles', '-pp', action='store_true', help='Prints List Of Profiles!')
    argument.add_argument('--assume-role', '-ar', action='store_true', help='Generates Temporary Credentials!')

    args = argument.parse_args()
    #argument.print_help()
    if args.print_profiles:
       print_profiles()
    if args.assume_role:
        a_role()
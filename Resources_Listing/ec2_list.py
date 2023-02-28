#!/usr/bin/env python3
import boto3
import pandas as pd

# Create an EC2 client object
ec2 = boto3.client('ec2')

# Retrieve a list of all regions
response = ec2.describe_regions()
regions = [region['RegionName'] for region in response['Regions']]

# Create an empty list to store instance information
instances = []

# Loop through all regions and retrieve instance information
for region in regions:
    # Retrieve a list of all instances in the current region
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances()
    
    # Extract instance information and store it in the list
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_dict = {
                'Name': '',
                'Size': '',
                'Tags': '',
                'Region': ''
            }
            instance_dict['Name'] = instance['InstanceId']
            instance_dict['Size'] = instance['InstanceType']
            instance_dict['Tags'] = instance['Tags']
            instance_dict['Region'] = region
            instances.append(instance_dict)

# Convert the list of dictionaries to a pandas dataframe
df = pd.DataFrame(instances)

# Export the dataframe to an Excel file
writer = pd.ExcelWriter('instances.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Instances', index=False)
writer.save()

print('Instances in all regions have been exported to instances.xlsx.')
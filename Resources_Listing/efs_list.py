#!/usr/bin/env python3
import boto3
import pandas as pd
from datetime import datetime

# Create a list of all the AWS regions
regions = [region['RegionName'] for region in boto3.client('ec2').describe_regions()['Regions']]

# Initialize a list to store EFS file system details
efs_list = []

# Iterate through each region and extract EFS details
for region in regions:
    # Create a Boto3 client for EFS in the region
    client = boto3.client('efs', region_name=region)

    # List all the EFS file systems in the region
    response = client.describe_file_systems()

    # Extract EFS details and append to the list
    for fs in response['FileSystems']:
        fs_id = fs['FileSystemId']
        fs_name = fs['Name']
        fs_creation_time = fs['CreationTime'].replace(tzinfo=None)  # Convert to timezone-naive datetime object
        fs_life_cycle_state = fs['LifeCycleState']
        fs_size_bytes = fs['SizeInBytes']['Value']
        fs_size_gb = round(fs_size_bytes / (1024**3), 2)  # Convert to GBs
        fs_performance_mode = fs['PerformanceMode']
        fs_throughput_mode = fs['ThroughputMode']
        fs_encryption = fs['Encrypted']

        # Append the extracted details to the list
        efs_list.append([region, fs_id, fs_name, fs_creation_time, fs_life_cycle_state, fs_size_gb, fs_performance_mode, fs_throughput_mode, fs_encryption])

# Create a Pandas DataFrame from the EFS list
efs_df = pd.DataFrame(efs_list, columns=['Region', 'ID', 'Name', 'CreationTime', 'LifeCycleState', 'Size (GB)', 'PerformanceMode', 'ThroughputMode', 'Encrypted'])

# Export the DataFrame to an Excel file
efs_df.to_excel('efs_list.xlsx', index=False)

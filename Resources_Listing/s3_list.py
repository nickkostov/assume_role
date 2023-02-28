#!/usr/bin/env python3
import boto3
import pandas as pd

# Create an S3 client object
s3 = boto3.client('s3')

# Retrieve a list of all buckets
response = s3.list_buckets()

# Extract bucket information and store it in a list of dictionaries
buckets = []
for bucket in response['Buckets']:
    bucket_dict = {
        'Name': '',
        'Type': '',
        'Region': '',
        'Access Type': ''
    }
    bucket_dict['Name'] = bucket['Name']
    bucket_dict['Type'] = 'Standard' if bucket['Name'].startswith('s3://') else 'S3'
    location = s3.get_bucket_location(Bucket=bucket['Name'])
    if location['LocationConstraint']:
        bucket_dict['Region'] = location['LocationConstraint']
    else:
        bucket_dict['Region'] = 'us-east-1'
    acl = s3.get_bucket_acl(Bucket=bucket['Name'])
    for grant in acl['Grants']:
        if grant.get('Grantee', {}).get('URI') == 'http://acs.amazonaws.com/groups/global/AllUsers':
            bucket_dict['Access Type'] = 'Public'
            break
    else:
        bucket_dict['Access Type'] = 'Private'
    buckets.append(bucket_dict)

# Convert the list of dictionaries to a pandas dataframe and sort it by name
df = pd.DataFrame(buckets).sort_values(by=['Name'])

# Export the dataframe to an Excel file
writer = pd.ExcelWriter('buckets.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Buckets', index=False)
writer.save()

print('S3 buckets have been exported to buckets.xlsx.')
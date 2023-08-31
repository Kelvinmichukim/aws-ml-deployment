import boto3

# Replace 'your_unique_bucket_name' with your desired bucket name
bucket_name = 'mwangihmod'

# Replace 'your_region' with your desired region, e.g., 'us-east-1'
my_region = 'us-west-2'  # Example: 'us-east-1'

s3 = boto3.client('s3', region_name=my_region)

try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': my_region
        }
    )
    print('S3 bucket created successfully')
except Exception as e:
    print('S3 error:', e)
import boto3
from botocore.exceptions import ClientError

def check_public_buckets():
    s3 = boto3.client("s3")
    buckets = []
    try:
        response = s3.list_buckets()
        for b in response['Buckets']:
            # Here you can add logic to check if bucket is public
            buckets.append(b['Name'])
    except ClientError as e:
        print(f"Error fetching buckets: {e}")
    return buckets

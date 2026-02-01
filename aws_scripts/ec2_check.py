import boto3
from botocore.exceptions import ClientError

def check_ec2_instances():
    ec2 = boto3.client("ec2")
    instances = []
    try:
        response = ec2.describe_instances()
        for r in response['Reservations']:
            for i in r['Instances']:
                instances.append(i['InstanceId'])
    except ClientError as e:
        print(f"Error fetching EC2 instances: {e}")
    return instances


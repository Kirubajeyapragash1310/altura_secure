import boto3

def check_open_ports(region="ap-south-1"):
    ec2 = boto3.client("ec2", region_name=region)
    open_instances = []

    try:
        response = ec2.describe_instances()
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instance_id = instance["InstanceId"]
                for sg in instance.get("SecurityGroups", []):
                    sg_info = ec2.describe_security_groups(GroupIds=[sg["GroupId"]])
                    for perm in sg_info["SecurityGroups"][0]["IpPermissions"]:
                        for ip_range in perm.get("IpRanges", []):
                            if ip_range.get("CidrIp") == "0.0.0.0/0":
                                open_instances.append(instance_id)
    except Exception as e:
        print(f"Error fetching EC2 instances: {e}")

    return open_instances

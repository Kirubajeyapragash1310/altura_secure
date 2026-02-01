import boto3

def check_public_buckets(region="ap-south-1"):
    s3 = boto3.client("s3", region_name=region)
    public_buckets = []

    try:
        buckets = s3.list_buckets()["Buckets"]
        for bucket in buckets:
            name = bucket["Name"]
            try:
                acl = s3.get_bucket_acl(Bucket=name)
                for grant in acl["Grants"]:
                    if "AllUsers" in str(grant):
                        public_buckets.append(name)
            except Exception:
                continue
    except Exception as e:
        print(f"Error fetching buckets: {e}")

    return public_buckets

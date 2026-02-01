import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from aws_scripts.s3_check import check_public_buckets
from aws_scripts.ec2_check import check_open_ports
from config import Config

def run_s3_security_check():
    buckets = check_public_buckets(Config.AWS_REGION)
    return {"status": "Risk" if buckets else "Safe", "issues": buckets}

def run_ec2_security_check():
    instances = check_open_ports(Config.AWS_REGION)
    return {"status": "Risk" if instances else "Safe", "issues": instances}

# Correct utils.py

import sqlite3
from aws_scripts.s3_check import check_public_buckets
from aws_scripts.ec2_check import check_ec2_instances

DB_PATH = "cloud_secure.db"

def get_total_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    conn.close()
    return count

def get_active_sessions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM sessions WHERE active=1")
    count = cursor.fetchone()[0]
    conn.close()
    return count

def get_security_status():
    public_buckets = check_public_buckets()
    return "Safe" if len(public_buckets) == 0 else "Warning"

def get_s3_usage():
    return "12 GB"

def get_recent_activities():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT activity FROM activities ORDER BY activity_time DESC LIMIT 5")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]

def get_alerts():
    alerts = []
    buckets = check_public_buckets()
    if buckets:
        alerts.append(f"{len(buckets)} public S3 buckets found!")
    instances = check_ec2_instances()
    if not instances:
        alerts.append("No EC2 instances running")
    return alerts



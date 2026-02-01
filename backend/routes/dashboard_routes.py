from flask import jsonify
from . import dashboard_bp
from utils import run_s3_security_check, run_ec2_security_check
from models.alert_model import Alert

@dashboard_bp.route("/api/dashboard", methods=["GET"])
def dashboard():
    s3_result = run_s3_security_check()
    ec2_result = run_ec2_security_check()

    alerts = []

    if s3_result["status"] == "Risk":
        for bucket in s3_result["issues"]:
            alerts.append(Alert(f"S3 bucket '{bucket}' is public", "High").to_dict())

    if ec2_result["status"] == "Risk":
        for inst in ec2_result["issues"]:
            alerts.append(Alert(f"EC2 instance '{inst}' open to 0.0.0.0/0", "High").to_dict())

    return jsonify({
        "security_status": "Risk" if alerts else "Safe",
        "alerts": alerts
    })

# backend/routes/dashboard_routes.py

from flask import Blueprint, jsonify
from backend.utils import (
    get_total_users,
    get_active_sessions,
    get_security_status,
    get_s3_usage,
    get_recent_activities,
    get_alerts
)

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/api")

@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard():
    data = {
        "total_users": get_total_users(),
        "active_sessions": get_active_sessions(),
        "security_status": get_security_status(),
        "s3_usage": get_s3_usage(),
        "recent_activities": get_recent_activities(),
        "alerts": get_alerts()
    }
    return jsonify(data)


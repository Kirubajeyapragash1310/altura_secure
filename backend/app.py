from flask import Flask, jsonify
from config import USE_DUMMY_DATA
from dummy_data import DUMMY_ALERTS

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/dashboard")
def dashboard():
    if USE_DUMMY_DATA:
        return jsonify({
            "security_status": "Warning",
            "alerts": DUMMY_ALERTS
        })

    return jsonify({
        "security_status": "Safe",
        "alerts": []
    })

if __name__ == "__main__":
    app.run(debug=True)




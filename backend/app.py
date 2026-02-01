# backend/app.py

from flask import Flask
from backend.routes.dashboard_routes import dashboard_bp

app = Flask(__name__)
app.register_blueprint(dashboard_bp)

@app.route("/")
def home():
    return "Flask is working!"

if __name__ == "__main__":
    app.run(debug=True)



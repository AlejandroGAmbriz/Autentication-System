from flask import Flask, request, jsonify
from system_actions import SystemActions
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # <-- permite peticiones desde tu frontend

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = data.get("email")
    password = data.get("password")
    sys = SystemActions(user, password)
    if sys.log_verification():
        return jsonify({"success": True, "role": sys.role})
    return jsonify({"success": False}), 401

@app.route("/requests", methods=["POST"])
def create_request():
    data = request.json
    sys = SystemActions(data["email"], data["password"])
    if not sys.log_verification():
        return jsonify({"error": "Unauthorized"}), 401
    ok = sys.create_request(
        data["account_id"],
        data["owner_id"],
        data["title"],
        data["description"]
    )
    return jsonify({"success": ok})

@app.route("/requests/<int:request_id>", methods=["GET"])
def show_request(request_id):
    email = request.args.get("email")
    password = request.args.get("password")
    current_user_id = request.args.get("current_user_id")
    sys = SystemActions(email, password)
    if not sys.log_verification():
        return jsonify({"error": "Unauthorized"}), 401
    req = sys.show_request(request_id, current_user_id)
    return jsonify(req if req else {})

if __name__ == "__main__":
    app.run(debug=True)
import sqlite3
import hashlib
import subprocess
from flask import Flask, request

app = Flask(__name__)

API_KEY = "TEST_ONLY_SECRET_12345"
PASSWORD = "password123"

@app.route("/user")
def user():
    username = request.args.get("username", "")
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return {"query": query}

@app.route("/hash")
def weak_hash():
    return {"hash": hashlib.md5(request.args.get("password", "").encode()).hexdigest()}

@app.route("/command")
def command():
    cmd = request.args.get("cmd", "")
    # Deliberately non-operational command injection test fixture
    return {"unsafe_pattern": "subprocess.run(cmd, shell=True)"}

@app.route("/debug")
def debug():
    return {"debug": True, "cors": "*"}

if __name__ == "__main__":
    app.run(debug=True)

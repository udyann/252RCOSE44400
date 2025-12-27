from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Path to stored message file
DATA_PATH = "/data/message.txt"


def read_message():
    """
    TODO: 
    - If DATA_PATH exists, read and return the text inside
    - If it doesn't exist, return an empty string
    """
    data = ''
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, 'r') as f:
            data = f.read()
    return data


def write_message(msg: str):
    """
    TODO:
    - Open DATA_PATH
    - Write msg to the file
    """
    with open(DATA_PATH, 'w') as f:
        f.write(msg)



@app.route("/api/message", methods=["GET"])
def get_message():
    """
    TODO:
    - Call read_message()
    - Return { "message": <stored message> } as JSON
    """
    message = read_message()
    return jsonify({ "message": message })


@app.route("/api/message", methods=["POST"])
def update_message():
    """
    TODO:
    - Get JSON from request
    - Extract the field "message"
    - Call write_message() to save it
    - Return { "status": "ok" }
    """
    data = request.get_json()
    message = str(data.get("message"))

    # added in V2
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    message = f'{message} (updated at {formatted_now})'
    write_message(message)
    return jsonify({ "status": "ok" })


# v1 has no /api/health endpoint
# (Students add this in v2)

# v2 TODO:
# - Modify write_message() or update_message() to include a timestamp
#   Format: "<message> (updated at YYYY-MM-DD HH:MM:SS)"
#
# - Add new endpoint /api/health that returns:
#   { "status": "healthy" }


@app.route("/api/health", methods=["GET"])
def get_health():
    return jsonify({ "status": "healthy" })


if __name__ == "__main__":
    # Do not change the host or port
    app.run(host="0.0.0.0", port=5001)

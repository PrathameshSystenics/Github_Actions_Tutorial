from flask import Flask, jsonify

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    """Add permissive CORS headers so the React app can call the API."""
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    return response


@app.route("/api/message", methods=["GET"])
def get_message():
    return jsonify({"message": "Hello from Flask API!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


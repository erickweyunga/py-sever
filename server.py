from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask Server</title>
</head>
<body>
    <h1>Hello from Flask!</h1>
    <p>This is a simple HTML response.</p>
</body>
</html>
"""


@app.route("/", methods=["GET"])
def index():
    client_ip = request.remote_addr
    logging.info(f"Received request from {client_ip} for /")
    return HTML_PAGE


if __name__ == "__main__":
    logging.info("Starting Flask server at http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)

import time
import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health_check():

    if random.random() < 0.5:
        return jsonify({"status": "error"}), 500 # HTTP internal server error 500

    if random.random() < 0.5:
        time.sleep(2)

    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
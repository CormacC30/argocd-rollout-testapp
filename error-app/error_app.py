import time
import random
from flask import Flask, jsonify, Response
from prometheus_client import Counter, Histogram, generate_latest

view_metric = Counter('health_check_requests', 'Total number of health check requests') # health metric

health_check_latency = Histogram("health_check_latency_seconds", "Latency of health check requests")

app = Flask(__name__)

@app.route("/health")
def health_check():

    if random.random() < 0.5:
        return jsonify({"status": "error"}), 500 # HTTP internal server error 500

    if random.random() < 0.5:
        time.sleep(2)

    # view metric
    view_metric.inc()
    return jsonify({"status": "healthy"}), 200

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
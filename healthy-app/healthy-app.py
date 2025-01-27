from flask import Flask, jsonify, Response
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

health_check_requests_total = Counter(
    "health_check_requests_total",
    "Total number of health check requests"
)
health_check_latency_seconds = Histogram(
    "health_check_latency_seconds",
    "Latency of health check requests"
)

@app.route("/health")
def health_check():
    health_check_requests_total.inc()
    return jsonify({"status": "healthy"}), 200

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
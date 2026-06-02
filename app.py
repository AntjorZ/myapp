from flask import Flask, jsonify

app = Flask(__name__)

# Имитация статистики запросов
request_counts = {
    "GET /": 0,
    "GET /status": 0,
    "GET /data": 0,
}

@app.route("/")
def home():
    request_counts["GET /"] += 1
    return jsonify({"message": "Hello, DevOps!"})

@app.route("/status")
def status():
    request_counts["GET /status"] += 1
    return jsonify({"status": "OK", "version": "1.0.0"})

@app.route("/data")
def data():
    request_counts["GET /data"] += 1
    return jsonify({"data": [1, 2, 3, 4, 5], "count": 5})

@app.route("/stats")
def stats():
    return jsonify(request_counts)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
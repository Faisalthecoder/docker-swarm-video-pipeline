from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(host="queue", port=6379)

@app.route("/upload", methods=["POST"])
def upload():
    data = request.json
    if not data or "video_name" not in data:
        return jsonify({"error": "Missing video_name"}), 400

    r.lpush("video_queue", data["video_name"])
    return jsonify({"status": "queued", "video": data["video_name"]}), 200

if __name__ == "__main__":
    # 👇 THIS keeps the container running
    app.run(host="0.0.0.0", port=5000, debug=True)


from flask import Flask, jsonify, render_template
from datetime import datetime, timezone
import os

app = Flask(__name__)

# Endpoint santé (utilisé par CI + Azure healthcheck)
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200

# Endpoint métier simple (testé en E2E)
@app.route("/api/greet/<name>", methods=["GET"])
def greet(name):
    if not name or name.strip() == "":
        return jsonify({"error": "name is required"}), 400
    return jsonify({"message": f"Hello, {name}!"}), 200

# Page d'accueil
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
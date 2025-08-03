from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
CONFIG_PATH = os.path.expanduser("~/jetstreamin/config/.jetconfig.json")

@app.route("/api/config", methods=["GET", "POST"])
def config():
    if request.method == "POST":
        with open(CONFIG_PATH, "w") as f:
            json.dump(request.json, f, indent=2)
        return jsonify({"status": "updated"})
    else:
        with open(CONFIG_PATH) as f:
            return jsonify(json.load(f))

app.run(host="0.0.0.0", port=5000)

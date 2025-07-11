# runner.py — Minimal Flask + Tor hidden service runner
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "This service runs in the dark. If you found it, you are meant to."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

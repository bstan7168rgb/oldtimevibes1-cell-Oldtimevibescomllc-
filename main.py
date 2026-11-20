from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
  <div style="padding: 2px 20px; font-family: system-ui">
    <h1 style="color: #5C6AC4;">Hello, World!</h1>
    <p>
      <a href="/api/hello" style="color: inherit;">API Demo</a>
    </p>
  </div>
"""


@app.route("/api/hello")
def hello():
    return jsonify(message="Hello, World!")
